from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import views
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiTypes

from .serializers import ResidentSerializer, ResidentCountSerializer
from .models import Resident


@extend_schema(tags=['residents'])
class ResidentViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResidentSerializer
    queryset = Resident.objects.all()
    
    
@extend_schema(
    tags=['residents-count'],
    responses=ResidentCountSerializer)
class ResidentCount(views.APIView):
    # serializer_class = ResidentCountSerializer
    def get(self, request, *args, **kwargs):
        
        count = Resident.objects.count()
        return Response({'total_residents': count})