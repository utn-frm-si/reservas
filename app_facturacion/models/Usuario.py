# coding=utf-8

from django.db import models


class Usuario(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    # Representación del objeto
    def __str__(self):
        return '{0!s}, {1!s}'.format(self.apellido, self.nombre)

    # Información de la clase
    class Meta:
        app_label = 'app_facturacion'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
