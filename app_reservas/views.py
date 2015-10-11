from django.shortcuts import get_object_or_404, render

from .models import Aula, Cuerpo, Nivel


def aula_detalle(request, num_cuerpo, num_nivel, num_aula):
    cuerpo = get_object_or_404(Cuerpo, numero=num_cuerpo)
    nivel = get_object_or_404(Nivel, cuerpo=cuerpo, numero=num_nivel)
    aula = get_object_or_404(Aula, nivel=nivel, numero=num_aula)
    return render(request, 'app_reservas/aula_detalle.html', {'aula': aula})


def index(request):
    return render(request, 'app_reservas/index.html')
