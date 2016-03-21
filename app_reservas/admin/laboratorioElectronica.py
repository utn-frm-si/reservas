# coding=utf-8

from django.contrib import admin

from ..models import LaboratorioElectronica


@admin.register(LaboratorioElectronica)
class LaboratorioElectronicaAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de LaboratorioElectronica en la interfaz de administración.
    """
    list_display = (
        'alias',
        'nombre',
        'capacidad',
        '_nivel',
        '_cuerpo',
        'archivo_ubicacion',
        'calendar_codigo',
        'calendar_color',
    )

    list_filter = (
        'nivel',
        'nivel__cuerpo',
    )

    def _nivel(self, obj):
        """
        Obtiene el nivel asociado a la instancia.
        """
        return obj.nivel.get_nombre_corto()
    _nivel.short_description = 'Nivel'
    _nivel.admin_order_field = 'nivel__numero'

    def _cuerpo(self, obj):
        """
        Obtiene el cuerpo asociado a la instancia.
        """
        return obj.nivel.cuerpo.get_nombre_corto()
    _cuerpo.short_description = 'Cuerpo'
    _cuerpo.admin_order_field = 'nivel__cuerpo__numero'
