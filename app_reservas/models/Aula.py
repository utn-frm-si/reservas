# coding=utf-8

from django.db import models


class Aula(models.Model):
    # Atributos
    numero = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50, blank=True)
    capacidad = models.PositiveSmallIntegerField()
    calendar_codigo = models.CharField(max_length=100)
    calendar_color = models.CharField(max_length=10)
    archivo_ubicacion = models.FileField(upload_to='ubicacion_aulas', blank=True)
    # Relaciones
    areas = models.ManyToManyField('Area')
    nivel = models.ForeignKey('Nivel')

    # Representación del objeto
    def __str__(self):
        return 'Aula %s - %s' % (self.numero, self.nivel)

    def get_nombre_corto(self):
        return 'Aula %s' % self.numero

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
