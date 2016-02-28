# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from app_reservas.models import Cuerpo, Nivel


class NivelDetailView(DetailView):
    model = Nivel
    context_object_name = 'nivel'

    def get_object(self, queryset=None):
        cuerpo = get_object_or_404(Cuerpo, numero=self.kwargs['numero_cuerpo'])
        return get_object_or_404(Nivel, cuerpo=cuerpo, numero=self.kwargs['numero_nivel'])
