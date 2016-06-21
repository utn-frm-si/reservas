# coding=utf-8

from django.db import models


class TipoLaboratorio(models.Model):
    # Atributos
    nombre = models.CharField(
        max_length=50,
        verbose_name='Nombre',
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='Slug',
        help_text='Etiqueta corta que identifica al tipo de laboratorio, y sólo puede contener '
                  'letras, números, guiones bajos y guiones medios. Generalmente es utilizada '
                  'para las direcciones URL. Por ejemplo, si el nombre del tipo de laboratorio es '
                  '"Química", un slug posible sería "quimica".',
    )

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['nombre']
        verbose_name = 'Tipo de laboratorio'
        verbose_name_plural = 'Tipos de laboratorio'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return self.nombre
