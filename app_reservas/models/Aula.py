# coding=utf-8

import os

from django.db import models
from django.template.defaultfilters import slugify

from .Recurso import Recurso


def establecer_destino_archivo_ubicacion(instance, filename):
    # Almacena el archivo en: 'app_reservas/ubicaciones/aulas/<nombre_completo_del_aula>.<extension>'
    ruta_archivos_ubicacion = 'app_reservas/ubicaciones/aulas/'
    extension_archivo = filename.split('.')[-1] if '.' in filename else ''
    nombre_archivo = '{0!s}.{1!s}'.format(slugify(str(instance)), extension_archivo)
    return os.path.join(ruta_archivos_ubicacion, nombre_archivo)


class Aula(Recurso):
    # Atributos
    numero = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=50, blank=True)
    capacidad = models.PositiveSmallIntegerField()
    archivo_ubicacion = models.FileField(upload_to=establecer_destino_archivo_ubicacion, blank=True)
    # Relaciones
    areas = models.ManyToManyField('Area')
    nivel = models.ForeignKey('Nivel')

    # Representación del objeto
    def __str__(self):
        return '{0!s} - {1!s}'.format(self.get_nombre_corto(), self.nivel)

    def get_nombre_corto(self):
        nombre_corto = self.nombre or 'Aula {0:d}'.format(self.numero)
        return nombre_corto

    # FIXME: Método necesario para que la migración funcione correctamente.
    @staticmethod
    def establecer_destino_archivo_ubicacion(instance, filename):
        return establecer_destino_archivo_ubicacion(instance, filename)

    # Información de la clase
    class Meta:
        app_label = 'app_reservas'
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
