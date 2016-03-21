# coding=utf-8

from django.db import models


class Nivel(models.Model):
    # Atributos
    numero = models.SmallIntegerField()
    # Relaciones
    cuerpo = models.ForeignKey('Cuerpo')

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return '{0!s} - {1!s}'.format(self.get_nombre_corto(), self.cuerpo)

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return 'Nivel {0:d}'.format(self.numero)

    def get_aulas(self):
        """
        Retorna el listado de aulas asociadas a la instancia.
        """
        return self.aula_set.order_by('numero', 'nombre')

    def get_laboratorios_informaticos(self):
        """
        Retorna el listado de laboratorios informáticos asociados a la instancia.
        """
        return self.laboratorioinformatico_set.all()
