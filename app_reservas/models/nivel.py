# coding=utf-8

from django.db import models

from ..services.recursos import get_recursos_asociados


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
        return '{0!s} - {1!s}'.format(self.get_nombre_corto(),
                                      self.cuerpo.get_nombre_corto())

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return 'Nivel {0:d}'.format(self.numero)

    def get_aulas(self):
        """
        Retorna el listado de aulas asociadas a la instancia.
        """
        return self.aula_set.all()

    def get_laboratorios_electronica(self):
        """
        Retorna el listado de laboratorios de Electrónica asociados a la instancia.
        """
        return self.laboratorioelectronica_set.all()

    def get_laboratorios_informatica(self):
        """
        Retorna el listado de laboratorios informáticos asociados a la instancia.
        """
        return self.laboratorioinformatico_set.all()

    def get_recursos(self):
        """
        Retorna todos los recursos asociados a la instancia.

        Returns
        -------
        list of dicts
            Lista de diccionarios, uno por cada tipo de recurso asociado que presenta al menos una
            instancia relacionada.
        """
        return get_recursos_asociados(self)
