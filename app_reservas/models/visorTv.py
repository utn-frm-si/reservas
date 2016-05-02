# coding=utf-8

from django.db import models

from ..services.recursos import (
    get_recursos_asociados,
    get_recursos_asociados_por_cuerpo,
)


class VisorTv(models.Model):
    # Atributos
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    # Relaciones
    area = models.ForeignKey('Area')
    aulas = models.ManyToManyField('Aula', blank=True)
    laboratorios_electronica = models.ManyToManyField('LaboratorioElectronica', blank=True)
    laboratorios_informatica = models.ManyToManyField('LaboratorioInformatico', blank=True)

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        verbose_name = 'Visor de TV'
        verbose_name_plural = 'Visores de TV'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return 'Visor de TV: {0!s}'.format(self.nombre)

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        return self.nombre

    def get_aulas(self):
        """
        Retorna el listado de aulas asociadas a la instancia.
        """
        return self.aulas.all()

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

    def get_recursos_por_cuerpo(self):
        """
        Retorna todos los recursos asociados a la instancia, separados por cuerpo.

        Returns
        -------
        list of dicts
            Lista de diccionarios, uno por cada cuerpo que presenta al menos una instancia
            relacionada.
        """
        return get_recursos_asociados_por_cuerpo(self)
