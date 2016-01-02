# coding=utf-8

from django.db import models

from .Recurso import Recurso


class LaboratorioInformatico(Recurso):
    # Atributos
    nombre = models.CharField(max_length=50)
    alias = models.CharField(max_length=10)
    capacidad = models.PositiveSmallIntegerField()
    # Relaciones
    nivel = models.ForeignKey('Nivel')

    # Representación del objeto
    def __str__(self):
        return 'Laboratorio informático: %s' % self.nombre

    def get_nombre_corto(self):
        return '%s (%s)' % (self.nombre, self.alias)

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
        verbose_name = 'Laboratorio informático'
        verbose_name_plural = 'Laboratorios informáticos'
