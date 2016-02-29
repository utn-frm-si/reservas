# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app_reservas.models import ProyectorMultimedia


class ProyectorMultimediaDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de ProyectorMultimedia.
    """
    model = ProyectorMultimedia
    context_object_name = 'proyector'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de ProyectorMultimedia cuyo identificador concuerda con el parámetro
        'identificador' de la URL, o una respuesta 404 en caso de ser inválido.
        """
        return get_object_or_404(ProyectorMultimedia, identificador=self.kwargs['identificador'])


class ProyectorMultimediaListView(ListView):
    """
    Vista de lista para todas las instancias existentes de ProyectorMultimedia, ordenadas por
    identificador.
    """
    model = ProyectorMultimedia
    context_object_name = 'proyectores'
    ordering = 'identificador'
