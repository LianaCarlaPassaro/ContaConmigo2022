from datetime import datetime

from django.db import models

# Create your models here.
from pacientes.models import Pacientes
from donantes.models import Donantes
from datetime import date

class ReposicionesAsignadas(models.Model):
    idPaciente = models.ForeignKey(Pacientes,on_delete=models.SET_NULL, null=True)
    idDonante = models.ForeignKey(Donantes, on_delete=models.SET_NULL, null=True)
    fechaReposicionElegida = models.DateField()
    comentario = models.TextField(max_length=1024)

    def __str__(self):
        return f'Paciente{self.idPaciente.nombre} id {self.idDonanteReposicion}'
