from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
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