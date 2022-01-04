from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_fin = models.DateField(blank=False, null=True)
    capacidad = models.CharField(max_length=100, null=False)
    numeros_de_horas = models.IntegerField(max_length=2, null=False)