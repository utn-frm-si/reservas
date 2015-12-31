# coding=utf-8

import json

from django.db import models

from app_reservas.adapters.google_calendar import obtener_eventos
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

    def get_eventos(self):
        return obtener_eventos(self.calendar_codigo)

    def get_eventos_json(self):
        eventos = self.get_eventos()
        eventos_json = '['
        primera_iteracion = True
        for evento in eventos:
            if primera_iteracion:
                primera_iteracion = False
            else:
                eventos_json += ','
            evento_str = json.dumps({
                'title': evento['titulo'],
                'start': evento['inicio_str'],
                'end': evento['fin_str'],
                'resourceId': str(self.id)
            })
            eventos_json += evento_str
        eventos_json += ']'
        return eventos_json

    # Información de la clase
    class Meta(Recurso.Meta):
        app_label = 'app_reservas'
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
