from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
    tipoDocumento = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.tipoDocumento}'
