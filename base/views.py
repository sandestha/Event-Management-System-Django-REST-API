from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,DjangoModelPermissions,IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token

from .models import User, Category, Venue, Events, Vendors, Attendees, Reservation, Tickets, Payment ,Reviews
from .serializers import GroupSerializers, UserSerializers, CategorySerializers, VendorSerializers, EventSerializers, VenueSerializers,AttendeeSerializers, ReservationSerializers, TicketSerializers, PaymentSerializers, ReviewSerializers

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
    permission_classes = [DjangoModelPermissions]

class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class VenueApiView(ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializers

class EventApiView(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

class VendorApiView(ModelViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorSerializers 

class AttendeeApiView(ModelViewSet):
    queryset = Attendees.objects.all()
    serializer_class = AttendeeSerializers

class ReservationApiView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers

class TicketApiView(ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketSerializers 

class PaymentApiView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class ReviewApiView(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAuthenticated,DjangoModelPermissions]