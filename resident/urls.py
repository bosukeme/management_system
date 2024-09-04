from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import  ResidentViewSet, ResidentCount

router = DefaultRouter()
router.register(r'residents', ResidentViewSet, basename='resident')


urlpatterns = [
    path('residents/count/', ResidentCount.as_view(), name='resident-count'),
    path("", include(router.urls)),
]
