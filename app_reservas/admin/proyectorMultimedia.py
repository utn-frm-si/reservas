# coding=utf-8

from django.contrib import admin

from ..models import ProyectorMultimedia


@admin.register(ProyectorMultimedia)
class ProyectorMultimediaAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de ProyectorMultimedia en la interfaz de administración.
    """
    list_display = (
        '_identificador',
        'calendar_codigo',
        'calendar_color',
    )

    def _identificador(self, obj):
        """
        Obtiene el identificador de la instancia.
        """
        return obj.get_nombre_corto()
    _identificador.short_description = 'Identificador'
    _identificador.admin_order_field = 'identificador'
