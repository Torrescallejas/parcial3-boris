from django.db import models

# Create your models here.
from django.db import models


class Celebraciones(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'celebraciones'


class Invitados(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    celebracion = models.ForeignKey(Celebraciones, models.DO_NOTHING, blank=True, null=True)
    presente = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invitados'