# coding=utf-8

from django.contrib import admin

from ..models import TipoLaboratorio


@admin.register(TipoLaboratorio)
class TipoLaboratorioAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de TipoLaboratorio en la interfaz de administración.
    """
    list_display = (
        'nombre',
        'slug',
    )
