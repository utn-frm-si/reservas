# coding=utf-8

from django.contrib import admin

from ..models import Nivel


@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de Nivel en la interfaz de administración.
    """
    list_display = (
        'numero',
        '_cuerpo',
    )

    def _cuerpo(self, obj):
        """
        Obtiene el cuerpo asociado a la instancia.
        """
        return obj.cuerpo
    _cuerpo.short_description = 'Cuerpo'
    _cuerpo.admin_order_field = 'cuerpo__numero'
