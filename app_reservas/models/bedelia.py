# coding=utf-8

from django.db import models

from ..services.recursos import get_recursos_asociados


class Bedelia(models.Model):
    # Relaciones
    area = models.OneToOneField('Area')
    aulas = models.ManyToManyField('Aula', blank=True)
    laboratorios_electronica = models.ManyToManyField('LaboratorioElectronica', blank=True)
    laboratorios_informatica = models.ManyToManyField('LaboratorioInformatico', blank=True)

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        verbose_name = 'Bedelía'
        verbose_name_plural = 'Bedelías'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return 'Bedelía: {0!s}'.format(str(self.area))

    def get_aulas(self):
        """
        Retorna el listado de aulas asociadas a la instancia.
        """
        return self.aulas.order_by('numero', 'nombre')

    def get_laboratorios_electronica(self):
        """
        Retorna el listado de laboratorios de Electrónica asociados a la instancia.
        """
        return self.laboratorios_electronica.all()

    def get_laboratorios_informatica(self):
        """
        Retorna el listado de laboratorios informáticos asociados a la instancia.
        """
        return self.laboratorios_informatica.all()

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
