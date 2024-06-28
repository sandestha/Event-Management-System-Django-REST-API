from rest_framework import serializers
from .models import Catering, Equipment, Transportation

class CateringSerializers(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = '__all__'

class EquipmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class TransportationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = '__all__'