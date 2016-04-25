# coding=utf-8

import os

from django.db import models
from django.template.defaultfilters import slugify

from .recurso import Recurso


def establecer_destino_archivo_ubicacion(instance, filename):
    """
    Establece la ruta de destino para el archivo de ubicación cargado a la instancia.
    """
    # Almacena el archivo en: 'app_reservas/ubicaciones/aulas/<nombre_completo>.<extension>'
    ruta_archivos_ubicacion = 'app_reservas/ubicaciones/aulas/'
    extension_archivo = filename.split('.')[-1] if '.' in filename else ''
    nombre_archivo = '{0!s}.{1!s}'.format(slugify(str(instance)), extension_archivo)
    return os.path.join(ruta_archivos_ubicacion, nombre_archivo)


class Aula(Recurso):
    # Atributos
    numero = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50, blank=True)
    capacidad = models.PositiveSmallIntegerField()
    archivo_ubicacion = models.FileField(upload_to=establecer_destino_archivo_ubicacion,
                                         blank=True)
    # Relaciones
    areas = models.ManyToManyField('Area')
    nivel = models.ForeignKey('Nivel')

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['nivel', 'numero', 'nombre']
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return '{0!s} - {1!s}'.format(self.get_nombre_corto(), self.nivel)

    def get_nombre_corto(self):
        """
        Retorna el nombre corto de la instancia.
        """
        nombre_corto = self.nombre or 'Aula {0:d}'.format(self.numero)
        return nombre_corto
