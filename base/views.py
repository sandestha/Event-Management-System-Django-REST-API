from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,DjangoModelPermissions,IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Category, Venue, Events, Vendors, Attendees, Reservation, Tickets, Reviews
from logistics.models import Catering,Equipment,Transportation
from .serializers import GroupSerializers, UserSerializers, CategorySerializers, VendorSerializers, EventSerializers, VenueSerializers,AttendeeSerializers, ReservationSerializers, TicketSerializers, ReviewSerializers
from django.conf import settings
import stripe
import requests

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def Register(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        obj = serializer.save()
        obj.password = hash_password
        obj.save()
        return Response('User Created !!')
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')     
    user = authenticate(username=email,password=password)

    if user == None:
        return Response('Invalid Credentials !!!')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)

@api_view(['POST'])
def Logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response('You have been Logged Out')

@api_view(['GET'])
def GroupListing(request):
    objs = Group.objects.all()
    serializer = GroupSerializers(objs,many = True)
    return Response(serializer.data)

class UserApiView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class VenueApiView(ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class EventApiView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    filterset_fields = ['category__name','category']
    search_fields = ['name']

class VendorApiView(ModelViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class AttendeeApiView(ModelViewSet):
    queryset = Attendees.objects.all()
    serializer_class = AttendeeSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class ReservationApiView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]



# class PaymentApiView(ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializers

class ReviewApiView(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]


@api_view(['GET'])
def RevenueReport(request, event_id):
    # def get(self, request, event_id):
    event = Events.objects.get(pk=event_id)
    venuecost = event.venue_cost 
    total_attendees = event.attendees.count()
    cost_based_on_attendees = event.Food_cost_per_person * total_attendees
    total_logistic_cost = (
        Catering.objects.filter(event=event).aggregate(total_logistic_cost=models.Sum('cost'))['total_logistic_cost'] +
        Equipment.objects.filter(event=event).aggregate(total_logistic_cost=models.Sum('cost'))['total_logistic_cost'] +
        Transportation.objects.filter(event=event).aggregate(total_logistic_cost=models.Sum('cost'))['total_logistic_cost'] 
    )
    total_revenue_from_tickets = (Tickets.objects.filter(event=event).aggregate(total_revenue_from_tickets=models.Sum('payment_amount'))['total_revenue_from_tickets'])
    total_event_cost = venuecost + cost_based_on_attendees + total_logistic_cost
    
    return Response({
        "Event Name": event.name,
        "Total Attendees": total_attendees,
        "Total Food Cost": cost_based_on_attendees,
        "Venue Cost":venuecost,
        "Total Logistic Cost": total_logistic_cost,
        "Total Revenue Generated From Ticket sales": total_revenue_from_tickets,
        "Total Event Cost":total_event_cost
        })

class TicketApiView(ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializers 
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class PaymentView(APIView):
    def post(self, request):
        try:
            # Retrieve data from the request
            payment_amount = request.data.get('payment_amount')
            ticket_no = request.data.get('ticket_no')
            event_id = request.data.get('event')
            attendee_id = request.data.get('attendee')
            payment_date = request.data.get('payment_date')
            payment_method = request.data.get('payment_method')
            stripe_token = request.data.get('stripe_token')

            # Retrieve Event and Attendee instances
            event = Events.objects.get(id=event_id)
            attendee = Attendees.objects.get(id=attendee_id)

            metadata = {
                'event_id': str(event.id),
                'attendee_id': str(attendee.id),
                'attendee_name': attendee.name,
                'event_name': event.name, 
            }

            # Create a charge using the Stripe API
            charge = stripe.Charge.create(
                amount=int(payment_amount * 100),
                currency='npr',
                source=stripe_token,
                description='Payment for ticket',
                metadata=metadata
            )
            
            
            ticket = Tickets.objects.create(
                payment_amount=payment_amount,
                ticket_no=ticket_no,
                event=event,
                attendee=attendee,
                payment_date=payment_date,
                payment_method=payment_method
            )
            
            # Return a success response
            return Response({'message': 'Payment successful'})

        except stripe.error.CardError as e:
            # Since it's a decline, stripe.error.CardError will be caught
            body = e.json_body
            err = body.get('error', {})
            return Response({'error': err.get('message')}, status=status.HTTP_400_BAD_REQUEST)
        
        except Events.DoesNotExist:
            return Response({'error': 'Event does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        except Attendees.DoesNotExist:
            return Response({'error': 'Attendee does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
