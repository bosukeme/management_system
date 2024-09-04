from rest_framework import serializers

from .models import PortalUser


class PortalUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = PortalUser
        fields = ["name", "phone_number", "email", "password"]
        
    def create(self, validated_data):
        user = PortalUser.objects.create_user(
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'], 
            password=validated_data['password'] 
        )
        
        return user


class PortalUserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
