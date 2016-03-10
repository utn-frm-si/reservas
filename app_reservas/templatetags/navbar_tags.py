from django import template

from ..models import (
    Area,
    Cuerpo,
)


register = template.Library()


@register.inclusion_tag('app_reservas/navbar.html')
def obtener_informacion_navbar():
    context = {
        'lista_cuerpos': Cuerpo.objects.all(),
        'lista_areas': Area.objects.all(),
    }
    return context
