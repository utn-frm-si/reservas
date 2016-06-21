# coding=utf-8

import json

from django.db import models

from ..adapters.google_calendar import generar_lista_eventos


class Recurso(models.Model):
    # Atributos
    calendar_codigo = models.CharField(
        max_length=100,
        verbose_name='ID del calendario',
        help_text='Puede conocerse al acceder a los detalles del calendario en Google Calendar. '
                  'Su formato habitual es: "identificador@group.calendar.google.com". '
                  'Por ejemplo, un valor válido es: '
                  '"pi4pfu4alasbojtd1v1bj32oc0@group.calendar.google.com".',
    )
    calendar_color = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Color del calendario',
        help_text='Color con el que se visualizan los eventos del calendario. '
                  'Debe estar en formato hexadecimal. Por ejemplo, un valor válido es: '
                  '"#ff8c0a"',
    )

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return '{0!s}'.format(self.get_nombre_corto())

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return 'Recurso: {0:d}'.format(self.id)

    def get_eventos(self):
        return generar_lista_eventos(self.calendar_codigo)

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
