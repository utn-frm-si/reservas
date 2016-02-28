# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app_reservas.models import ProyectorMultimedia


class ProyectorMultimediaDetailView(DetailView):
    model = ProyectorMultimedia
    context_object_name = 'proyector'

    def get_object(self, queryset=None):
        return get_object_or_404(ProyectorMultimedia, identificador=self.kwargs['identificador'])


class ProyectorMultimediaListView(ListView):
    model = ProyectorMultimedia
    context_object_name = 'proyectores'
    ordering = 'identificador'
