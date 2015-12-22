# coding=utf-8

from django.shortcuts import get_object_or_404, render

from .models import Area, Aula, Cuerpo, Nivel


def area_detalle(request, slug_area):
    # Obtiene el área por su nombre.
    area = get_object_or_404(Area, slug=slug_area)
    return render(
        request,
        'app_reservas/area_detalle.html',
        {
            'area': area,
        }
    )


def aula_detalle(request, aula_id):
    # Obtiene el aula.
    aula = get_object_or_404(Aula, id=aula_id)
    return render(
        request,
        'app_reservas/aula_detalle.html',
        {
            'aula': aula,
        }
    )


def nivel_detalle(request, num_cuerpo, num_nivel):
    # Obtiene el cuerpo.
    cuerpo = get_object_or_404(Cuerpo, numero=num_cuerpo)
    # Obtiene el nivel.
    nivel = get_object_or_404(Nivel, cuerpo=cuerpo, numero=num_nivel)
    return render(
        request,
        'app_reservas/nivel_detalle.html',
        {
            'nivel': nivel,
        }
    )


def cuerpo_detalle(request, num_cuerpo):
    # Obtiene el cuerpo.
    cuerpo = get_object_or_404(Cuerpo, numero=num_cuerpo)
    return render(
        request,
        'app_reservas/cuerpo_detalle.html',
        {
            'cuerpo': cuerpo,
        }
    )


def index(request):
    return render(
        request,
        'app_reservas/index.html'
    )


def solicitud_aula(request):
    return render(
        request,
        'app_reservas/solicitud_aula.html'
    )
