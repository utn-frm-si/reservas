# coding=utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models import (
    Bedelia,
    Cuerpo,
)


class TvBedeliaDetailView(DetailView):
    """
    Vista de detalle para la visualización en TV de una instancia específica de Bedelia.
    """
    model = Bedelia
    context_object_name = 'bedelia'
    template_name = 'app_reservas/tv_bedelia.html'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de Bedelia que tiene asociada el área cuyo slug concuerda con el
        parámetro 'area_slug' de la URL, o una respuesta 404 en caso de ser inválido.
        """
        return get_object_or_404(Bedelia, area__slug=self.kwargs['area_slug'])

    def get_context_data(self, **kwargs):
        """
        Añade al contexto la información de cuerpo y nivel especificados
        mediante parámetros GET.
        """
        # Obtiene la información de contexto base.
        context = super(TvBedeliaDetailView, self).get_context_data(**kwargs)
        # Obtiene los parámetros GET de cuerpo y nivel especificados.
        cuerpo = self.request.GET.get('cuerpo')
        nivel = self.request.GET.get('nivel')
        # Convierte los parámetros a entero y los añade al contexto, sólo en
        # caso de que se hayan especificado y sean números.
        if cuerpo and cuerpo.isdigit():
            context['cuerpo_solicitado'] = int(cuerpo)
        if nivel and nivel.isdigit():
            context['nivel_solicitado'] = int(nivel)
        # Retorna el contexto modificado.
        return context


class TvBedeliaCuerposDetailView(DetailView):
    """
    Vista de detalle para la visualización en TV de una instancia específica de Bedelia, con sus
    recursos ordenados por cuerpo.
    """
    model = Bedelia
    context_object_name = 'bedelia'
    template_name = 'app_reservas/tv_bedelia_cuerpos.html'

    def get_object(self, **kwargs):
        """
        Retorna la instancia de Bedelia que tiene asociada el área cuyo slug concuerda con el
        parámetro 'area_slug' de la URL, o una respuesta 404 en caso de ser inválido.
        """
        return get_object_or_404(Bedelia, area__slug=self.kwargs['area_slug'])


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
