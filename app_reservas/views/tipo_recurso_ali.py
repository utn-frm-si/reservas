# coding=utf-8

from django.views.generic.detail import DetailView

from ..models import TipoRecursoAli


class TipoRecursoAliDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de TipoRecursoAli.
    """
    model = TipoRecursoAli
    context_object_name = 'tipo_recurso'
