from django.db import models

# Create your models here.
class Provincia(models.Model):
    nombreProvincia = models.CharField(max_length=255)

    def __str__(self):
        return f' {self.nombreProvincia}'