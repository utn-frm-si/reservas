# coding=utf-8

from django.views.generic.list import ListView

from app_reservas.models import Cuerpo


class TvCuerposListView(ListView):
    model = Cuerpo
    context_object_name = 'cuerpos'
    template_name = 'app_reservas/tv_cuerpos.html'

    def get_queryset(self):
        # Obtiene por parámetro GET 'numero' los números de cuerpos a mostrar. En
        # caso de no especificarse, se muestran todos los cuerpos.
        cuerpos_solicitados = self.request.GET.getlist('numero')

        if cuerpos_solicitados:
            # Filtra los cuerpos para obtener los solicitados.
            cuerpos = Cuerpo.objects.filter(numero__in=cuerpos_solicitados)
        else:
            # Obtiene todos los cuerpos.
            cuerpos = Cuerpo.objects

        # Retorna los cuerpos, ordenados por número.
        return cuerpos.order_by('numero')
