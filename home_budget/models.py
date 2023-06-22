from django.db import models
from django.utils import timezone

class wydatek(models.Model):
    nazwa = models.CharField(max_length=50)
    kategoria = models.CharField(max_length=50)
    kwota = models.FloatField()
    data_powstania = models.DateTimeField(default=timezone.now)

class przychod(models.Model):
    nazwa = models.CharField(max_length=50)
    kategoria = models.CharField(max_length=50)
    kwota = models.FloatField()
    data_powstania = models.DateTimeField(default=timezone.now)
