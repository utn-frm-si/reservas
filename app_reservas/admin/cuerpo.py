# coding=utf-8

from django.contrib import admin

from ..models import Cuerpo


@admin.register(Cuerpo)
class CuerpoAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de Cuerpo en la interfaz de administración.
    """
    list_display = (
        'numero',
        'nombre',
        '_niveles',
    )

    def _niveles(self, obj):
        """
        Obtiene el listado de niveles asociados a la instancia.
        """
        return ", ".join([nivel.get_nombre_corto() for nivel in obj.nivel_set.all()])
    _niveles.short_description = 'Niveles'
