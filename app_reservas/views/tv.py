# coding=utf-8

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import (
    Area,
    Cuerpo,
)


class TvAreaDetailView(DetailView):
    """
    Vista de detalle para la visualización en TV de una instancia específica de Area.
    """
    model = Area
    context_object_name = 'area'
    template_name = 'app_reservas/tv_area.html'


class TvCuerposListView(ListView):
    """
    Vista de lista para la visualización en TV de instancias de Cuerpo, ordenadas por número.
    """
    model = Cuerpo
    context_object_name = 'cuerpos'
    template_name = 'app_reservas/tv_cuerpos.html'

    def get_queryset(self):
        """
        Retorna las instancias de Cuerpo cuyo número se encuentra especificado en el parámetro GET
        'numero' de la URL, o todos los cuerpos en caso de que el parámetro no sea especificado.
        Los cuerpos son ordenados por número.
        """
        # Obtiene por parámetro GET 'numero' los números de cuerpos a mostrar. En
        # caso de no especificarse, se muestran todos los cuerpos.
        cuerpos_solicitados = self.request.GET.getlist('numero')

        if cuerpos_solicitados:
            # Filtra los cuerpos para obtener los solicitados.
            cuerpos = Cuerpo.objects.filter(numero__in=cuerpos_solicitados)
        else:
            # Obtiene todos los cuerpos.
            cuerpos = Cuerpo.objects

        # Retorna los cuerpos, ordenados por número (el ordenamiento está definido a nivel de
        # modelo).
        return cuerpos.all()
