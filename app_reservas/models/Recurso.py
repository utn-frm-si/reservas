# coding=utf-8

from django.db import models


class Recurso(models.Model):
    # Atributos
    calendar_codigo = models.CharField(max_length=100)
    calendar_color = models.CharField(max_length=10, blank=True)

    # Representación del objeto
    def __str__(self):
        return '%s' % self.get_nombre_corto()

    def get_nombre_corto(self):
        return 'Recurso: %d' % self.id

    # Información de la clase
    class Meta:
        abstract = True
        app_label = 'app_reservas'
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
