from django.db import models

# Create your models here.

class GrupoFactor(models.Model):
    gruposFactorDescripcion = models.CharField(max_length=255)

    def __str__(self):
        return f'Grupo/Factor: {self.gruposFactorDescripcion}'


