# coding=utf-8

from django.db import models

from .Recurso import Recurso


class Aula(Recurso):
    # Atributos
    numero = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50, blank=True)
    capacidad = models.PositiveSmallIntegerField()
    archivo_ubicacion = models.FileField(upload_to='ubicacion_aulas', blank=True)
    # Relaciones
    areas = models.ManyToManyField('Area')
    nivel = models.ForeignKey('Nivel')

    # Representación del objeto
    def __str__(self):
        return '%s - %s' % (self.get_nombre_corto(), self.nivel)

    def get_nombre_corto(self):
        nombre_corto = ''
        if self.nombre is None or self.nombre == '':
            nombre_corto = 'Aula %s' % self.numero
        else:
            nombre_corto = self.nombre
        return nombre_corto

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
