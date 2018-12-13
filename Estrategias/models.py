from django.db import models

class Estrategia(models.Model):
    Estrategia_id = models.IntegerField(default=0)
    Hay_estrategia_asignaturas = models.BooleanField(default=False)
    Hay_estrategia_posgrado = models.BooleanField(default=False)
    Descripcion = models.TextField(default="", blank=True, null=True)
