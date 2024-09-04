from django.urls import path, include
from rest_framework import routers
from .views import PortalUserViewSet

router = routers.DefaultRouter()
router.register(r'portal-users', PortalUserViewSet, basename='portal-user')

urlpatterns = [
    path("", include(router.urls)),
]
