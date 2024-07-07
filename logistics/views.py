from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from base.models import *
from .models import Catering, Equipment, Transportation
from .serializers import CateringSerializers, EquipmentSerializers, TransportationSerializers

# Create your views here.
class CateringApiView(ModelViewSet):
    queryset = Catering.objects.all()
    serializer_class = CateringSerializers

class EquipmentApiView(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializers

class TransportApiView(ModelViewSet):
    queryset = Transportation.objects.all()
    serializer_class = EquipmentSerializers

@api_view(['GET'])
def LogisticTotal(request, event_id):
    # def get(self, request, event_id):
    event = Events.objects.get(pk=event_id)
    total_cost = (
        Catering.objects.filter(event=event).aggregate(total_cost=models.Sum('cost'))['total_cost'] +
        Equipment.objects.filter(event=event).aggregate(total_cost=models.Sum('cost'))['total_cost'] +
        Transportation.objects.filter(event=event).aggregate(total_cost=models.Sum('cost'))['total_cost'] 
    )
    return Response({"Event Name":event.name, "TotaL Logistic Cost":total_cost})

# @api_view(['GET'])
# def Report(request,event_id):
#     Total = LogisticTotal(event_id)
#     return Response({'Logistics Total Cost':Total})

# @api_view(['GET'])
# def Report(self, event_id):
#     response = LogisticTotal(event_id)
#     return Response(response)

class Report(APIView):
    def get(self,request,event_id):
        response = LogisticTotal(event_id)
        return Response(response)
