# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from app_reservas.models import Cuerpo


class CuerpoDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de Cuerpo.
    """
    model = Cuerpo
    context_object_name = 'cuerpo'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de Cuerpo cuyo número concuerda con el parámetro 'numero' de la URL, o
        una respuesta 404 en caso de ser inválido.
        """
        return get_object_or_404(Cuerpo, numero=self.kwargs['numero'])
