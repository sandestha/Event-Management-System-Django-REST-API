from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User ,Category, Venue, Events, Vendors, Attendees, Reservation, Tickets, Payment,Reviews

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password','groups']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class VenueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = '__all__'

class AttendeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendees
        fields = '__all__'

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'