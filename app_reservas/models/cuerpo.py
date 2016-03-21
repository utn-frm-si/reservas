# coding=utf-8

from django.db import models


class Cuerpo(models.Model):
    # Atributos
    numero = models.PositiveSmallIntegerField()

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['numero']
        verbose_name = 'Cuerpo'
        verbose_name_plural = 'Cuerpos'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return '{0!s}'.format(self.get_nombre_corto())

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return 'Cuerpo {0:d}'.format(self.numero)

    def get_niveles(self):
        """
        Retorna el listado de niveles asociados a la instancia.
        """
        return self.nivel_set.order_by('numero')
