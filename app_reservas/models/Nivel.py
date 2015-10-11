# coding=utf-8

from django.db import models


class Nivel(models.Model):
    # Atributos
    numero = models.SmallIntegerField()
    # Relaciones
    cuerpo = models.ForeignKey('Cuerpo')

    # Representación del objeto
    def __str__(self):
        return 'Nivel %s - Cuerpo %s' % (self.numero, self.cuerpo.numero)

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
