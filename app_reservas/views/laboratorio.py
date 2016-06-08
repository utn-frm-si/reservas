# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from ..models import (
    Laboratorio,
    TipoLaboratorio,
)


class LaboratorioDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de Laboratorio.
    """
    model = Laboratorio
    context_object_name = 'laboratorio'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de Laboratorio cuyo alias y tipo concuerdan con
        los parámetros 'alias' y 'tipo' de la URL, o una respuesta 404 en caso
        de ser inválido.
        """
        tipo_laboratorio = get_object_or_404(TipoLaboratorio, slug=self.kwargs['tipo'])
        return get_object_or_404(Laboratorio, tipo=tipo_laboratorio, alias=self.kwargs['alias'])
