# coding=utf-8

from django.db import models


class TipoRecursoAli(models.Model):
    # Atributos
    nombre = models.CharField(
        max_length=50,
        verbose_name='Nombre',
        help_text='Nombre del tipo de recurso, en singular.',
    )
    nombre_plural = models.CharField(
        max_length=50,
        verbose_name='Nombre en plural',
        help_text='Nombre del tipo de recurso, en plural.',
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='Slug',
        help_text='Etiqueta corta que identifica al tipo de recurso, y sólo puede contener '
                  'letras, números, guiones bajos y guiones medios. Generalmente es utilizada '
                  'para las direcciones URL. Por ejemplo, si el nombre del tipo de recurso es '
                  '"Proyectores multimedia", un slug posible sería "proyectores" o '
                  '"proyectores_multimedia".',
    )
    prefijo = models.CharField(
        max_length=5,
        verbose_name='Prefijo',
        help_text='Prefijo del tipo de recurso, utilizado en los identificadores de los recursos '
                  'de dicho tipo. Por ejemplo, el prefijo "PM" es propio del tipo de recurso '
                  '"Proyector multimedia", ya que todos los recursos de este tipo tienen un '
                  'identificador que comienza con "PM".',
    )
    is_sufijo = models.BooleanField(
        default=False,
        verbose_name='¿Es sufijo?',
        help_text='Indica si el prefijo indicado en realidad se utiliza como sufijo.',
    )
    is_visible_navbar = models.BooleanField(
        default=False,
        verbose_name='Visible en la navbar',
        help_text='Indica si el tipo de recurso se lista dentro de las opciones del ALI, en la '
                  'navbar (barra de navegación superior) del sitio.',
    )

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['nombre']
        verbose_name = 'Tipo de recurso del ALI'
        verbose_name_plural = 'Tipos de recurso del ALI'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return self.nombre
