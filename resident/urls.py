from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddVisitorToResidentView, ListVisitorsForResidentView
from .views import  ResidentViewSet

router = DefaultRouter()
router.register(r'residents', ResidentViewSet, basename='resident')



urlpatterns = [
    path("", include(router.urls)),
    path('residents/<int:resident_id>/add-visitor/', AddVisitorToResidentView.as_view(), name='add-visitor-to-resident'),
    path('residents/<int:resident_id>/visitors/', ListVisitorsForResidentView.as_view(), name='list-visitors-for-resident'),
]
