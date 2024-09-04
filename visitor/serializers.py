from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from .models import Visitor, VisitSession

from resident.models import Resident


class VisitorSerializer(serializers.ModelSerializer):
    
    @extend_schema_field(serializers.CharField) 
    def get_fullname(self):
        return self.instance.fullname
    
    class Meta:
        model = Visitor
        fields = ['id', 'surname', 'other_name', 'fullname', "phone_number", "email", "address"]        


class VisitSessionSerializer(serializers.ModelSerializer):
    
    visitor = serializers.PrimaryKeyRelatedField(queryset=Visitor.objects.all(), write_only=True)
    resident = serializers.PrimaryKeyRelatedField(queryset=Resident.objects.all(), write_only=True)
    
    visitor_fullname = serializers.SerializerMethodField()
    visitor_phone_number = serializers.SerializerMethodField()
    visitor_email = serializers.SerializerMethodField()
    check_in = serializers.DateTimeField(read_only=True)
        
    class Meta:
        model = VisitSession
        fields = ['id', 'visitor', 'resident', 'visitor_fullname', 'visitor_phone_number', 'visitor_email', 'check_in']
        read_only_fields = ['check_in']

    def get_visitor_fullname(self, obj) -> str:
        return obj.visitor.fullname
    
    def get_visitor_phone_number(self, obj) -> str:
        return obj.visitor.phone_number

    def get_visitor_email(self, obj) -> str:
        return obj.visitor.email

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request', None)
        
        # Exclude 'check_in' for POST requests
        if request and request.method == 'POST':
            representation.pop('check_in', None)
        
        return representation


class CheckOutSerializer(serializers.ModelSerializer):

    resident = serializers.PrimaryKeyRelatedField(queryset=Resident.objects.all(), write_only=True)

    class Meta:
        model = VisitSession
        fields = ['id', 'resident', 'check_out']
        read_only_fields = ['check_out']