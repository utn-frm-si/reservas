# coding=utf-8

from django.db import models


class Area(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

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
