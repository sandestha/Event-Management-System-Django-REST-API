from django.urls import path
from .views import CateringApiView,LogisticTotal, Report
urlpatterns = [
    path('catering/',CateringApiView.as_view({'get':'list','post':'create'}),name='catering'),
    path('report/<int:event_id>/',Report.as_view()),
    path('total/<int:event_id>/',LogisticTotal),
    
]