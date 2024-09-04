from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import  VisitorViewSet, ListVisitorsForResidentView, CheckOutView, VisitSessionView, OpenVisitorCount, DailyVisitorCount

router = DefaultRouter()
router.register(r'visitors', VisitorViewSet, basename='visitor')


urlpatterns = [
    path('residents/<int:resident_id>/visitors/', ListVisitorsForResidentView.as_view(), name='list-visitors-for-resident'),
    path('visitors/<int:pk>/checkout/', CheckOutView.as_view(), name='visitor-checkout'),
    path('visitors/session/', VisitSessionView.as_view(), name='visit-session'),
    path('visitors/open/', OpenVisitorCount.as_view(), name='open-session'),
    path('daily-visitor-count/', DailyVisitorCount.as_view(), name='daily-visitor-count'),
    path("", include(router.urls)),
]
