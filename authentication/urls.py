from django.urls import path, include
from rest_framework import routers
from .views import VisitorViewSet

router = routers.DefaultRouter()
router.register(r'visitors', VisitorViewSet, basename='visitor')

urlpatterns = [
    path("", include(router.urls)),
]
