from rest_framework import serializers
from .models import ResidentVisitor

from .models import Resident, Visitor


class ResidentVisitorSerializer(serializers.ModelSerializer):
    visitor = serializers.PrimaryKeyRelatedField(queryset=Visitor.objects.all())
    resident = serializers.PrimaryKeyRelatedField(queryset=Resident.objects.all(), write_only=True) 
    
    
    class Meta:
        model = ResidentVisitor
        fields = ['id', 'visitor', 'resident', 'check_in', 'check_out']


class ResidentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resident
        fields = ['id', 'name', "room_number"]