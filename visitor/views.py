from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions

from drf_spectacular.utils import extend_schema

from authentication.models import Visitor
from authentication.serializers import VisitorSerializer

from resident.models import ResidentVisitor

from resident.serializers import ResidentVisitorSerializer
from  resident.models import Resident



@extend_schema(tags=['visitor'])
class VisitorDetailView(generics.RetrieveAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class CheckInView(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = ResidentVisitor.objects.all()
    serializer_class = ResidentVisitorSerializer

    def create(self, request, *args, **kwargs):
        resident = Resident.objects.get(pk=kwargs['resident_id'])
        visitor = Visitor.objects.get(pk=kwargs['visitor_id'])
        visit = ResidentVisitor.objects.create(resident=resident, visitor=visitor)
        serializer = self.get_serializer(visit)
        return Response(serializer.data)


class CheckOutView(generics.UpdateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = ResidentVisitor.objects.all()
    serializer_class = ResidentVisitorSerializer

    def update(self, request, *args, **kwargs):
        visit = self.get_object()
        visit.check_out = timezone.now()  # Set check-out time to current time
        visit.save()
        serializer = self.get_serializer(visit)
        return Response(serializer.data)
