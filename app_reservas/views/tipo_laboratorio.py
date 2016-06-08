# coding=utf-8

from django.views.generic.detail import DetailView

from ..models import TipoLaboratorio


class TipoLaboratorioDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de Area.
    """
    model = TipoLaboratorio
    context_object_name = 'tipo_laboratorio'
