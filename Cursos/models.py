from django.db import models


class Programa(models.Model):
    programa_id = models.fields.IntegerField(default=0)
    nombre = models.fields.CharField(max_length=200, blank=True, null=True)
    beneficios = models.fields.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    institucion = 'Institucional'
    unidad_academica = 'Unidad academica'
    programa = 'Programa'
    externo = 'Externo'
    elecciones_responsabilidades = ((institucion, 'Institucional'),
                                    (unidad_academica, 'Unidad academica'),
                                    (programa, 'Programa'),
                                    (externo, 'Externo'))

    curso_id = models.fields.IntegerField(default=0)
    nombre = models.fields.CharField(max_length=200, blank=True, null=True)
    responsabilidad = models.fields.CharField(max_length=20, choices=elecciones_responsabilidades, default='')
    ultimo_anio = models.fields.IntegerField(blank=True, null=True)
    penultimo_anio = models.fields.IntegerField(blank=True, null=True)
    antepenultimo_anio = models.fields.IntegerField(blank=True, null=True)
    numero_participantes = models.fields.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Desarrollo(models.Model):
    desarrollo_id = models.fields.IntegerField(default=0)
    institucion = 'Institucional'
    unidad_academica = 'Unidad academica'
    programa = 'Programa'
    elecciones_responsabilidades = ((institucion, 'Institucional'),
                                    (unidad_academica, 'Unidad academica'),
                                    (programa, 'Programa'))

    hay_plan_permanente_superacion = models.fields.BooleanField(default=False)

    hay_programas_superacion = models.fields.BooleanField(default=False)

    hay_otra_modalidad = models.fields.BooleanField(default=False)
    descripcion_modalidad = models.TextField(default="", blank=True, null=True)

    hay_plan_formacion = models.fields.BooleanField(default=False)
    nivel_responsabilidad = models.fields.CharField(max_length=20, choices=elecciones_responsabilidades, default='Elegir')
    descripcion_formacion = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        return "Desarrollo"
