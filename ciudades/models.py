from django.db import models

# Create your models here.
from provincia.models import Provincia


class Ciudad(models.Model):
    nombreCiudad = models.CharField(max_length=255)
    codigoPostal = models.IntegerField()
    idProvincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Ciudad: {self.nombreCiudad} Provincia: {self.idProvincia}'
