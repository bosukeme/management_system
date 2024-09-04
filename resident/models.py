from django.db import models
from django.utils import timezone

from authentication.models import Visitor


class Resident(models.Model):
    name = models.CharField(max_length=50, null=False)
    room_number = models.IntegerField(null=False)


class ResidentVisitor(models.Model):
    
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    check_in = models.DateTimeField(default=timezone.now)  # Automatically set the check-in time
    check_out = models.DateTimeField(null=True, blank=True)  

    def __str__(self) -> str:
        return self.visitor.name
    