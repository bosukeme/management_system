from django.urls import path, include
from .views import  VisitorDetailView
from .views import CheckInView, CheckOutView


urlpatterns = [
    path('visitors/<int:pk>/', VisitorDetailView.as_view(), name='visitor-detail'),
    path('residents/<int:resident_id>/visitors/<int:visitor_id>/check-in/', CheckInView.as_view(), name='check-in'),
    path('residents/<int:resident_id>/visitors/<int:visitor_id>/check-out/', CheckOutView.as_view(), name='check-out'),
]
