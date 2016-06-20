# coding=utf-8

import os

from django.db import models


def establecer_destino_archivo_imagen(instance, filename):
    """
    Establece la ruta de destino para el archivo de imagen cargado a la instancia.
    """
    # Almacena el archivo en:
    # 'app_reservas/carruseles/<carrusel>/<imagen>'
    ruta_archivos_ubicacion = 'app_reservas/carruseles/{}/'.format(
        instance.carrusel.slug,
    )
    return os.path.join(ruta_archivos_ubicacion, filename)


class ImagenCarrusel(models.Model):
    # Atributos
    orden = models.PositiveSmallIntegerField(default=1)
    imagen = models.ImageField(upload_to=establecer_destino_archivo_imagen)
    # Relaciones
    carrusel = models.ForeignKey('CarruselImagenes', related_name='imagenes')

    class Meta:
        """
        Información de la clase.
        """
        app_label = 'app_reservas'
        ordering = ['carrusel', 'orden']
        verbose_name = 'Imagen de carrusel'
        verbose_name_plural = 'Imágenes de carrusel'

    def __str__(self):
        """
        Representación de la instancia.
        """
        return "Imagen {0:d} del carrusel '{1!s}'".format(
            self.orden,
            self.carrusel,
        )

    def get_url(self):
        """
        Retorna la URL de la imagen.
        """
        return self.imagen.url
