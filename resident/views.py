from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import viewsets

from .models import ResidentVisitor
from .serializers import ResidentVisitorSerializer, ResidentSerializer


from .models import Resident

@extend_schema(tags=['visitor'])
class AddVisitorToResidentView(generics.CreateAPIView):
    serializer_class = ResidentVisitorSerializer

    def post(self, request, *args, **kwargs):
        resident_id = self.kwargs.get('resident_id')
        data = request.data.copy()  # Use copy to avoid modifying the original request data
        data['resident'] = resident_id  # Add the resident_id to the data
        
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['visitor'])
class ListVisitorsForResidentView(generics.ListAPIView):
    serializer_class = ResidentVisitorSerializer

    def get_queryset(self):
        resident_id = self.kwargs.get('resident_id')
        return ResidentVisitor.objects.filter(resident_id=resident_id)


@extend_schema(tags=['residents'])
class ResidentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResidentSerializer
    queryset = Resident.objects.all()