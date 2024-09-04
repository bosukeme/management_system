from rest_framework import serializers

from .models import Visitor

from resident.models import Resident
from resident.serializers import ResidentSerializer

class VisitorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Visitor
        fields = ["name", "phone_number", "email", "password"]
        
    def create(self, validated_data):
        user = Visitor.objects.create_user(
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'], 
            password=validated_data['password'] 
        )
        
        return user


class VisitorLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)


class VisitorSerializer(serializers.ModelSerializer):
    visited_residents = serializers.SerializerMethodField()

    class Meta:
        model = Visitor
        fields = ['id', 'name', 'phone_number', 'email', 'visited_residents']

    def get_visited_residents(self, obj):
        # Retrieve residents visited by this visitor
        queryset = Resident.objects.filter(residentvisitor__visitor=obj)
        return ResidentSerializer(queryset, many=True).data
