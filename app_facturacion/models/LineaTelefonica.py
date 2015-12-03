# coding=utf-8

from django.db import models


class LineaTelefonica(models.Model):
    # Atributos
    numero = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=50, blank=True)
    # Relaciones
    area = models.ForeignKey('Area')
    usuario = models.ForeignKey('Usuario')

    # Representación del objeto
    def __str__(self):
        return '%s' % str(self.numero)

    # Información de la clase
    class Meta:
        app_label = 'app_facturacion'
        verbose_name = 'Línea telefónica'
        verbose_name_plural = 'Líneas telefónicas'
