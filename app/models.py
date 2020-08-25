from django.db import models

class Emisora(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.CharField(max_length=150)
    generos = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre