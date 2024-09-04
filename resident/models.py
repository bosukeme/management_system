from django.db import models
from django.utils import timezone


class Resident(models.Model):
    name = models.CharField(max_length=50, null=False)
    room_number = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.name