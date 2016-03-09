# coding=utf-8

from django.contrib import admin

from ..models import LaboratorioInformatico


@admin.register(LaboratorioInformatico)
class LaboratorioInformaticoAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de LaboratorioInformatico en la interfaz de administración.
    """
    list_display = (
        'alias',
        'nombre',
        'capacidad',
        'archivo_ubicacion',
        'nivel',
        'calendar_codigo',
        'calendar_color',
    )
