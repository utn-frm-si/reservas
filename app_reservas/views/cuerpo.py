# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from app_reservas.models import Cuerpo


class CuerpoDetailView(DetailView):
    model = Cuerpo
    context_object_name = 'cuerpo'

    def get_object(self, queryset=None):
        return get_object_or_404(Cuerpo, numero=self.kwargs['numero'])
