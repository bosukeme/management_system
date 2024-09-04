from django.db import models
from django.utils import timezone
from resident.models import Resident


class Visitor(models.Model):
    surname = models.CharField(max_length=50, null=False)
    other_name = models.CharField(max_length=50, null=False)
    phone_number = models.IntegerField(null=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=500, null=False)
    
    def __str__(self) -> str:
        return self.surname
    
    @property
    def fullname(self) -> str:
        return f"{self.surname} {self.other_name}"


class VisitSession(models.Model):
    
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    
    check_in = models.DateTimeField(default=timezone.now)  # Automatically set the check-in time
    check_out = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.visitor.surname} is visiting {self.resident.name}"
