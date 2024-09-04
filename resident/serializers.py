from rest_framework import serializers
from .models import Resident



class ResidentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resident
        fields = ['id', 'name', "room_number"]

class ResidentCountSerializer(serializers.Serializer):
    total_residents = serializers.IntegerField()