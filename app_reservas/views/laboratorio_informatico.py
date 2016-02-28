# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from app_reservas.models import LaboratorioInformatico


class LaboratorioInformaticoDetailView(DetailView):
    model = LaboratorioInformatico
    context_object_name = 'laboratorio'

    def get_object(self, queryset=None):
        return get_object_or_404(LaboratorioInformatico, alias=self.kwargs['alias'])


class LaboratorioInformaticoListView(ListView):
    model = LaboratorioInformatico
    context_object_name = 'laboratorios'
    ordering = 'alias'
