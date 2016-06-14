# coding=utf-8

from django.contrib import admin

from ..models import TipoRecursoAli


@admin.register(TipoRecursoAli)
class TipoRecursoAliAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de TipoRecursoAli en la interfaz de administración.
    """
    list_display = (
        'nombre',
        'nombre_plural',
        'slug',
        'prefijo',
        'is_sufijo',
        'is_visible_navbar',
    )

    list_filter = (
        'is_visible_navbar',
    )
