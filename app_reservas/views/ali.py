# coding=utf-8

from django.views.generic.detail import DetailView

from ..models import Aula


class AliVideoconferenciasDetailView(DetailView):
    """
    Vista de detalle para la sala de videoconferencias del ALI.
    """
    model = Aula
    context_object_name = 'aula'

    def get_object(self):
        # Obtiene la instancia de la sala de videoconferencias.
        return Aula.objects.filter(
            nivel__cuerpo__numero=6,
            nivel__numero=2,
            numero=1,
        ).first()
