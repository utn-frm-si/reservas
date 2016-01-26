# coding=utf-8

from django.db import models


class PlanLinea(models.Model):
    # Atributos
    cantidad_total = models.PositiveIntegerField()
    cantidad_cubierta = models.PositiveIntegerField()
    # Relaciones
    linea = models.ForeignKey('LineaTelefonica')
    tipo_concepto = models.ForeignKey('TipoConcepto')

    # Representación del objeto
    def __str__(self):
        return '<PlanLinea>: {0!s}'.format(str(self.id))

    # Información de la clase
    class Meta:
        app_label = 'app_facturacion'
        verbose_name = 'Plan de línea'
        verbose_name_plural = 'Planes de línea'
