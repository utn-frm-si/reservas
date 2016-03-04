# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import LaboratorioElectronica


class LaboratorioElectronicaDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de LaboratorioElectronica.
    """
    model = LaboratorioElectronica
    context_object_name = 'laboratorio'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de LaboratorioElectronica cuyo alias concuerda con el parámetro
        'alias' de la URL, o una respuesta 404 en caso de ser inválido.
        """
        return get_object_or_404(LaboratorioElectronica, alias=self.kwargs['alias'])


class LaboratorioElectronicaListView(ListView):
    """
    Vista de lista para todas las instancias existentes de LaboratorioElectronica, ordenadas por
    alias.
    """
    model = LaboratorioElectronica
    context_object_name = 'laboratorios'
    ordering = 'alias'
