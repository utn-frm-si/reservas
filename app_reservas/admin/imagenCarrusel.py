# coding=utf-8

from django.contrib import admin

from ..models import ImagenCarrusel


@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de ImagenCarrusel en la interfaz de administración.
    """
    list_display = (
        '_carrusel',
        'orden',
        'imagen',
    )

    list_filter = (
        'carrusel',
    )

    def _carrusel(self, obj):
        """
        Obtiene el carrusel asociado a la instancia.
        """
        return str(obj.carrusel)
    _carrusel.short_description = 'Carrusel'
    _carrusel.admin_order_field = 'carrusel__nombre'
