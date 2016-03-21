# coding=utf-8

from django.db import models

from .recurso import Recurso


class ProyectorMultimedia(Recurso):
    # Atributos
    identificador = models.CharField(max_length=20)

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['identificador']
        verbose_name = 'Proyector multimedia'
        verbose_name_plural = 'Proyectores multimedia'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return 'Proyector multimedia: {0!s}'.format(self.get_nombre_corto())

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return 'PM-{0!s}'.format(self.identificador)
