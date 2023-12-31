from django.db import models
from django.utils import timezone
from django.conf import settings

class Transakcja(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=50)
    kategoria = models.CharField(max_length=50)
    kwota = models.FloatField()
    data_powstania = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = "Transakcja"
        verbose_name_plural = "Transakcje"

class Wydatek(Transakcja):
    pass
    class Meta:
        verbose_name = "Wydatek"
        verbose_name_plural = "Wydatki"

class Przychod(Transakcja):
    pass
    class Meta:
        verbose_name = "Przychod"
        verbose_name_plural = "Przychody"