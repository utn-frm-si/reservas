# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from ..models import (
    RecursoAli,
    TipoRecursoAli,
)


class RecursoAliDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de RecursoAli.
    """
    model = RecursoAli
    context_object_name = 'recurso'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de RecursoAli cuyo alias y tipo concuerdan con
        los parámetros 'identificador' y 'tipo' de la URL, o una respuesta 404
        en caso de ser inválido.
        """
        tipo_recurso = get_object_or_404(TipoRecursoAli, slug=self.kwargs['tipo'])
        return get_object_or_404(
            RecursoAli,
            tipo=tipo_recurso,
            identificador=self.kwargs['identificador'],
        )
