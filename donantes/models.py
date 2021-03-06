from django.db import models

# Create your models here.

from ciudades.models import Ciudad
from gruposFactor.models import GrupoFactor
from sexo.models import Sexo
from tipoDocumentos.models import TipoDocumento


class Donantes(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    sexo = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)
    tipoDNI = models.ForeignKey(TipoDocumento,on_delete=models.SET_NULL, null=True)
    dni = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    tipoSangre = models.ForeignKey(GrupoFactor, on_delete=models.SET_NULL, null=True)
    fechaUltimaExtraccion = models.DateField()
    mail = models.CharField(max_length=255)


    def __str__(self):
        return f'Donante: Nombre {self.nombre} Apellido: {self.apellido}'