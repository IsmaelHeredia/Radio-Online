from django.db import models
import datetime

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Emisora(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    genero = models.ForeignKey(Genero)
    fecha_registro = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.fecha_registro is None:
            self.fecha_registro = datetime.datetime.now()
        super(Emisora, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre