# coding=utf-8

from django.db import models


class TipoConcepto(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    tarifa = models.DecimalField(max_digits=7, decimal_places=3)

    # Representación del objeto
    def __str__(self):
        return '%s' % self.nombre

    # Información de la clase
    class Meta:
        app_label = 'app_facturacion'
        verbose_name = 'Tipo de concepto'
        verbose_name_plural = 'Tipos de concepto'
