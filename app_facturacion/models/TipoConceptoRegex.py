# coding=utf-8

from django.db import models


class TipoConceptoRegex(models.Model):
    # Atributos
    regex = models.CharField(max_length=128)
    # Relaciones
    tipo_concepto = models.ForeignKey('TipoConcepto')

    # Representación del objeto
    def __str__(self):
        return '%s' % str(self.id)

    # Información de la clase
    class Meta:
        app_label = 'app_facturacion'
        verbose_name = 'Expresión regular para tipo de concepto'
        verbose_name_plural = 'Expresiones regulares para tipo de concepto'
