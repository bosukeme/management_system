from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone 

from .serializers import VisitorSerializer, CheckOutSerializer, VisitSessionSerializer
from .models import Visitor, VisitSession


@extend_schema(tags=['visitors'])
class VisitorViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = VisitorSerializer
    queryset = Visitor.objects.all()
    
    
@extend_schema(tags=['visitor'])
class ListVisitorsForResidentView(generics.ListAPIView):

    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = VisitorSerializer

    def get_queryset(self):
        resident_id = self.kwargs.get('resident_id')
        return Visitor.objects.filter(resident_id=resident_id)
    

@extend_schema(tags=['visitor checkout'])
class CheckOutView(generics.UpdateAPIView):

    # permission_classes = [permissions.IsAuthenticated]
    queryset = VisitSession.objects.all()
    serializer_class = CheckOutSerializer

    def update(self, request, *args, **kwargs):
        visitor_id = kwargs.get('pk')
        resident_id = request.data.get('resident')
        
        if not resident_id:
            return Response(
                {"detail": "Resident ID is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
                
        try:
            visit_session = VisitSession.objects.get(
                visitor_id=visitor_id,
                resident_id=resident_id,
                check_out__isnull=True
            )
        except VisitSession.DoesNotExist:
            return Response(
                {"detail": "Visitor is not checked in with this resident or already checked out."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        visit_session.check_out = timezone.now()
        visit_session.save()
        
        serializer = self.get_serializer(visit_session)
        return Response(serializer.data)


@extend_schema(tags=['Visit Session'])
class VisitSessionView(generics.ListCreateAPIView, generics.RetrieveDestroyAPIView):

    # permission_classes = [permissions.IsAuthenticated]
    queryset = Visitor.objects.all()
    serializer_class = VisitSessionSerializer



@extend_schema(
    tags=['open visitor count'],)
class OpenVisitorCount(views.APIView):

    def get(self, request, *args, **kwargs):
        
        open_visitors_count = VisitSession.objects.filter(check_out__isnull=True).count()
        return Response({'total_open_visitors': open_visitors_count})
    
    
@extend_schema(tags=['daily visitor count'])
class DailyVisitorCount(views.APIView):

    def get(self, request, *args, **kwargs):
        # Get the current date
        current_date = timezone.now().date()
        
        # Filter visit sessions where check_in date matches the current date
        daily_visitors = VisitSession.objects.filter(check_in__date=current_date)
        daily_visitors_count = daily_visitors.count()
        
        # You can also return more detailed information if needed
        # For simplicity, returning just the count here
        return Response({
            'total_daily_visitors': daily_visitors_count,
            'visitors': [
                {
                    'visitor_id': session.visitor.id,
                    'resident_id': session.resident.id,
                    'check_in': session.check_in,
                }
                for session in daily_visitors
            ]
        })