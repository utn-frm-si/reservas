# coding=utf-8

from django.db import models


class TipoRecursoAli(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    nombre_plural = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    prefijo = models.CharField(max_length=5)
    is_sufijo = models.BooleanField(default=False)
    is_visible_navbar = models.BooleanField(default=False)

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
