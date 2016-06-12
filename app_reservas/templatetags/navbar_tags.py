# coding=utf-8

from django import template

from ..models import (
    Area,
    Aula,
    Cuerpo,
    TipoLaboratorio,
)


register = template.Library()


@register.inclusion_tag('app_reservas/navbar.html')
def obtener_informacion_navbar():
    # Obtiene la instancia de la sala de videoconferencias.
    sala_videoconferencias = Aula.objects.filter(
        nivel__cuerpo__numero=6,
        nivel__numero=2,
        numero=1,
    ).first()

    context = {
        'lista_cuerpos': Cuerpo.objects.all(),
        'lista_areas': Area.objects.all(),
        'lista_tipos_laboratorio': TipoLaboratorio.objects.all(),
        'sala_videoconferencias': sala_videoconferencias,
    }
    return context
