from django.contrib import admin
from .models import User, Category, Venue, Events,Attendees,Vendors,Reservation,Tickets,Payment,Reviews
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Venue)
admin.site.register(Events)
admin.site.register(Attendees)
admin.site.register(Vendors)
admin.site.register(Reservation)
admin.site.register(Tickets)
admin.site.register(Payment)
admin.site.register(Reviews)