from django.db import models

# Create your models here.
from ciudades.models import Ciudad


class Institucion(models.Model):
    nombreInstitucion = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    idCiudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombreInstitucion} - {self.idCiudad}'