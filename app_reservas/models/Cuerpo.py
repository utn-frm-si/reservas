# coding=utf-8

from django.db import models


class Cuerpo(models.Model):
    # Atributos
    numero = models.PositiveSmallIntegerField()

    # Representación del objeto
    def __str__(self):
        return 'Cuerpo %s' % self.numero

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
