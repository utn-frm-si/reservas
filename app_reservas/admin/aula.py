# coding=utf-8

from django.contrib import admin

from ..models import Aula


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de Aula en la interfaz de administración.
    """
    list_display = (
        '_nombre',
        'capacidad',
        '_nivel',
        '_cuerpo',
        'archivo_ubicacion',
        '_areas',
        'calendar_codigo',
        'calendar_color',
    )

    def _nombre(self, obj):
        """
        Obtiene el nombre de la instancia.
        """
        return obj.get_nombre_corto()
    _nombre.short_description = 'Nombre'
    _nombre.admin_order_field = 'numero'

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

    def _areas(self, obj):
        """
        Obtiene el listado de áreas asociadas a la instancia.
        """
        return ", ".join([area.nombre for area in obj.areas.order_by('nombre')])
    _areas.short_description = 'Áreas'
