# coding=utf-8

from django.db import models

from .Recurso import Recurso


class ProyectorMultimedia(Recurso):
    # Atributos
    identificador = models.CharField(max_length=20)

    # Representación del objeto
    def __str__(self):
        return 'Proyector multimedia: %s' % self.get_nombre_corto()

    def get_nombre_corto(self):
        return 'PM-%s' % self.identificador

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
        verbose_name = 'Proyector multimedia'
        verbose_name_plural = 'Proyectores multimedia'
