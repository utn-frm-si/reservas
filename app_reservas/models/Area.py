# coding=utf-8

from django.db import models


class Area(models.Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    # Representación del objeto
    def __str__(self):
        return self.nombre

    def get_aulas(self):
        return self.aula_set.order_by('numero')

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
