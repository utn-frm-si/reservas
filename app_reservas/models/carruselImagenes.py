# coding=utf-8

from django.db import models


class CarruselImagenes(models.Model):
    # Atributos
    nombre = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(unique=True, max_length=50)
    ancho_maximo = models.PositiveSmallIntegerField(default=800)

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
