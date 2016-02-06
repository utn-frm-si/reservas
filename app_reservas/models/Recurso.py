# coding=utf-8

import json

from django.db import models

from app_reservas.adapters.google_calendar import obtener_eventos


class Recurso(models.Model):
    # Atributos
    calendar_codigo = models.CharField(max_length=100)
    calendar_color = models.CharField(max_length=10, blank=True)

    # Representación del objeto
    def __str__(self):
        return '{0!s}'.format(self.get_nombre_corto())

    def get_nombre_corto(self):
        return 'Recurso: {0:d}'.format(self.id)

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
                eventos_json += ',\n'
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
    class Meta:
        app_label = 'app_reservas'
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
