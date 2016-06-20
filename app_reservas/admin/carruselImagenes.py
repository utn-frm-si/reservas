# coding=utf-8

from django.contrib import admin

from ..models import CarruselImagenes


@admin.register(CarruselImagenes)
class CarruselImagenesAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de CarruselImagenes en la interfaz de administración.
    """
    list_display = (
        'nombre',
        'slug',
        'ancho_maximo',
    )
