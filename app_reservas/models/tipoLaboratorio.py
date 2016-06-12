# coding=utf-8

from django.db import models


class TipoLaboratorio(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

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
