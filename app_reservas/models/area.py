# coding=utf-8

from django.db import models


class Area(models.Model):
    # Atributos
    nombre = models.CharField(
        max_length=50,
        verbose_name='Nombre',
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='Slug',
        help_text='Etiqueta corta que identifica al área, y sólo puede contener letras, números, '
                  'guiones bajos y guiones medios. Generalmente es utilizada para las direcciones '
                  'URL. Por ejemplo, si el nombre del área es "Dirección TIC", un slug posible '
                  'sería "ditic" o "direccion_tic".',
    )

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['nombre']
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return self.nombre

    def get_aulas(self):
        """
        Retorna el listado de aulas asociadas a la instancia.
        """
        return self.aula_set.all()
