# coding=utf-8

from django.views.generic.detail import DetailView

from ..models import Aula


class AulaDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de Aula.
    """
    model = Aula
    context_object_name = 'aula'
