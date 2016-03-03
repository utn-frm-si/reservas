# coding=utf-8

from django.views.generic.detail import DetailView

from ..models import Area


class AreaDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de Area.
    """
    model = Area
    context_object_name = 'area'
