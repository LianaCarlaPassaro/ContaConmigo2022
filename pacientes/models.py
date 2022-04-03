from django.db import models

# Create your models here.
from ciudades.models import Ciudad
from gruposFactor.models import GrupoFactor
from instituciones.models import Institucion
from tipoDocumentos.models import TipoDocumento


class Pacientes(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    tipoDNI = models.ForeignKey(TipoDocumento,on_delete=models.SET_NULL, null=True)
    dni = models.CharField(max_length=255)
    fechaNacimiento = models.DateField()
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    institucion = models.ForeignKey(Institucion,  on_delete=models.SET_NULL, null=True)
    fechaLimite = models.DateField()
    cantidadDonantes = models.IntegerField()
    mail = models.CharField(max_length=255)
    comentario = models.TextField(max_length=1024)
    completo = models.BooleanField(default=False)
    telefono = models.CharField(max_length=255)
    tipoSangre = models.ForeignKey(GrupoFactor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Nombre: {self.nombre} Apellido: {self.apellido} '