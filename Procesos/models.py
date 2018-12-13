from django.db import models


class Proceso(models.Model):
    Proceso = models.fields.CharField(max_length=200, blank=False, default="")
    Existe_proceso_formal = models.BooleanField(default=False)
    Descripcion_Proceso = models.TextField(default="", blank=True, null=True)
    Hay_reglamento = models.BooleanField(default=False)
    evidencia = models.FileField(upload_to="evidencias/", null=True, blank=True, )

    def __str__(self):
        return self.Proceso
