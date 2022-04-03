from django.db import models

# Create your models here.
from provincia.models import Provincia


class Ciudad(models.Model):
    nombreCiudad = models.CharField(max_length=255)
    codigoPostal = models.IntegerField()
    idProvincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = 'ciudad'

    def __str__(self):
        return f'{self.nombreCiudad} - {self.idProvincia}'
