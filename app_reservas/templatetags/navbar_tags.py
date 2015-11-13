from django import template

from app_reservas.models import Area, Aula, Cuerpo, Nivel

register = template.Library()


@register.inclusion_tag('app_reservas/navbar.html')
def obtener_informacion_navbar():
    context = {
        'lista_cuerpos': Cuerpo.objects.all(),
    }
    return context
