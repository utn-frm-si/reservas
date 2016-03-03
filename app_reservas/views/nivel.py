# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

from ..models import Cuerpo, Nivel


class NivelDetailView(DetailView):
    """
    Vista de detalle para una instancia específica de Nivel.
    """
    model = Nivel
    context_object_name = 'nivel'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de Nivel asociada al cuerpo especificado por el parámetro
        'numero_cuerpo', y cuyo número concuerda con el parámetro 'numero_nivel' de la URL.

        En caso de ser inválido alguno de los parámetros, retorna una respuesta 404.
        """
        cuerpo = get_object_or_404(Cuerpo, numero=self.kwargs['numero_cuerpo'])
        return get_object_or_404(Nivel, cuerpo=cuerpo, numero=self.kwargs['numero_nivel'])
