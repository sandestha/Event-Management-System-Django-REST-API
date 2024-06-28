from django.urls import path
from .views import UserApiView,GroupListing, Login, Logout, Register, ReviewApiView,EventApiView,AttendeeApiView,CategoryApiView,VenueApiView,VendorApiView,ReservationApiView,TicketApiView,PaymentApiView
from logistics.views import CateringApiView,TransportApiView,EquipmentApiView
urlpatterns = [
    path('users/',UserApiView.as_view({'get':'list'})),
    path('roles/',GroupListing),
    path('login/',Login),
    path('logout/',Logout),
    path('register/',Register),
    path('events/',EventApiView.as_view({'get':'list','post':'create'}),name='events'),
    path('events/<int:pk>',EventApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='events_details'),
    path('attendees/',AttendeeApiView.as_view({'get':'list','post':'create'}),name='attendees'),
    path('attendees/<int:pk>',AttendeeApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='attendees_details'),
    path('category/',CategoryApiView.as_view({'get':'list','post':'create'}),name='category'),
    path('category/<int:pk>',CategoryApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='category_details'),
    path('venue/',VenueApiView.as_view({'get':'list','post':'create'}),name='venue'),
    path('venue/<int:pk>',VenueApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='venue_details'),
    path('vendor/',VendorApiView.as_view({'get':'list','post':'create'}),name='vendor'),
    path('vendor/<int:pk>',VendorApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='vendor_details'),
    path('reservation/',ReservationApiView.as_view({'get':'list','post':'create'}),name='reservation'),
    path('reservation/<int:pk>',ReservationApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='reservation_details'),
    path('ticket/',TicketApiView.as_view({'get':'list','post':'create'}),name='ticket'),
    path('ticket/<int:pk>',TicketApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='ticket_details'),
    path('payment/',PaymentApiView.as_view({'get':'list','post':'create'}),name='payment'),
    path('payment/<int:pk>',PaymentApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='payment_details'),
    path('feedback/',ReviewApiView.as_view({'get':'list','post':'create'}),name='feedback'),
    path('feedback/<int:pk>',ReviewApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='feedback_details'),

    path('catering/',CateringApiView.as_view({'get':'list','post':'create'}),name='catering'),
    path('catering/<int:pk>',CateringApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='catering_details'),
    path('transport/',TransportApiView.as_view({'get':'list','post':'create'}),name='transport'),
    path('transport/<int:pk>',TransportApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='transport_details'),
    path('equipment/',EquipmentApiView.as_view({'get':'list','post':'create'}),name='equipment'),
    path('equipment/<int:pk>',EquipmentApiView.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='equipment_details'),

    
]