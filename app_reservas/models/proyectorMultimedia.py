# coding=utf-8

from django.db import models

from .recurso import Recurso


class ProyectorMultimedia(Recurso):
    # Atributos
    identificador = models.CharField(max_length=20)

    # Representación del objeto
    def __str__(self):
        return 'Proyector multimedia: {0!s}'.format(self.get_nombre_corto())

    def get_nombre_corto(self):
        return 'PM-{0!s}'.format(self.identificador)

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
        ordering = ['identificador']
        verbose_name = 'Proyector multimedia'
        verbose_name_plural = 'Proyectores multimedia'
