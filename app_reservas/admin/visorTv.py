# coding=utf-8

from django.contrib import admin

from ..models import VisorTv


@admin.register(VisorTv)
class VisorTvAdmin(admin.ModelAdmin):
    """
    Especificación de la representación de VisorTv en la interfaz de administración.
    """
    list_display = (
        'nombre',
        'slug',
        '_area',
        '_aulas',
        '_laboratorios',
        '_laboratorios_informatica',
    )

    def _area(self, obj):
        """
        Obtiene el área asociada a la instancia.
        """
        return str(obj.area)
    _area.short_description = 'Área'

    def _aulas(self, obj):
        """
        Obtiene el listado de aulas asociadas a la instancia.
        """
        return ", ".join(
            [str(aula)
             for aula in obj.aulas.all()]
        )
    _aulas.short_description = 'Aulas'

    def _laboratorios(self, obj):
        """
        Obtiene el listado de laboratorios de Ingeniería asociados a la instancia.
        """
        return ", ".join(
            [laboratorio.get_nombre_corto()
             for laboratorio in obj.laboratorios.all()]
        )
    _laboratorios.short_description = 'Laboratorios de Ingeniería'

    def _laboratorios_informatica(self, obj):
        """
        Obtiene el listado de laboratorios informáticos asociados a la instancia.
        """
        return ", ".join(
            [laboratorio.get_nombre_corto()
             for laboratorio in obj.laboratorios_informatica.all()]
        )
    _laboratorios_informatica.short_description = 'Laboratorios informáticos'
