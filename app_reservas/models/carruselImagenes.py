# coding=utf-8

from django.db import models


class CarruselImagenes(models.Model):
    # Atributos
    nombre = models.CharField(
        unique=True,
        max_length=50,
        verbose_name='Nombre',
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Slug',
        help_text='Etiqueta corta que identifica al carrusel, y sólo puede contener letras, '
                  'números, guiones bajos y guiones medios.'
    )
    ancho_maximo = models.PositiveSmallIntegerField(
        default=800,
        verbose_name='Ancho máximo',
        help_text='Ancho máximo del carrusel, medido en píxeles (px).'
    )

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['nombre']
        verbose_name = 'Carrusel de imágenes'
        verbose_name_plural = 'Carruseles de imágenes'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return self.nombre

    def get_imagenes(self):
        """
        Retorna el listado de imágenes asociadas a la instancia.
        """
        return self.imagenes.all()
