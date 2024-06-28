from django.urls import path
from .views import CateringApiView
urlpatterns = [
    path('catering/',CateringApiView.as_view({'get':'list','post':'create'}),name='catering'),
]