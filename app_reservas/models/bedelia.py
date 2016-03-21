# coding=utf-8

from django.db import models

from .aula import Aula
from .laboratorioElectronica import LaboratorioElectronica
from .laboratorioInformatico import LaboratorioInformatico


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
        """Retorna todos los recursos asociados a la instancia.

        Genera una lista conformada por diccionarios, uno por cada tipo de recurso asociado. Cada
        uno de estos diccionarios indica los nombres apropiados del tipo de recurso, y una lista
        con las instancias de ese tipo que están relacionadas a la instancia.
        En caso de que la instancia no tenga recursos relacionados de un cierto tipo, el
        diccionario de este tipo no es añadido a la lista.

        Returns
        -------
        list of dicts
            Lista de diccionarios, uno por cada tipo de recurso asociado que presenta al menos una
            instancia relacionada.
        """
        recursos = []

        # Añade las aulas asociadas, en caso de existir.
        if self.get_aulas():
            recursos.append(
                {
                    'nombre_singular': Aula._meta.verbose_name,
                    'nombre_plural': Aula._meta.verbose_name_plural,
                    'slug': 'aulas',
                    'elementos': self.get_aulas(),
                }
            )
        # Añade los laboratorios de Electrónica asociados, en caso de existir.
        if self.get_laboratorios_electronica():
            recursos.append(
                {
                    'nombre_singular': LaboratorioElectronica._meta.verbose_name,
                    'nombre_plural': LaboratorioElectronica._meta.verbose_name_plural,
                    'slug': 'laboratorios_electronica',
                    'elementos': self.get_laboratorios_electronica(),
                }
            )
        # Añade los laboratorios de informática asociados, en caso de existir.
        if self.get_laboratorios_informatica():
            recursos.append(
                {
                    'nombre_singular': LaboratorioInformatico._meta.verbose_name,
                    'nombre_plural': LaboratorioInformatico._meta.verbose_name_plural,
                    'slug': 'laboratorios_informatica',
                    'elementos': self.get_laboratorios_informatica(),
                }
            )

        return recursos
