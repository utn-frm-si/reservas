# coding=utf-8

import json
from datetime import date
from dateutil.parser import parse

from django.http import JsonResponse
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


def aula_eventos_json(request, aula_id):
    # Indica la ruta donde se almacenan los archivos JSON de eventos de aulas.
    ruta_archivos = 'media/app_reservas/eventos_aulas/'

    # Obtiene el aula especificada.
    aula = get_object_or_404(Aula, id=aula_id)

    # Arma el nombre del archivo.
    nombre_archivo = str(aula.id) + '.json'
    nombre_archivo_completo = ruta_archivos + nombre_archivo

    # Inicializa la lista de eventos a retornar.
    eventos = []

    # Lee el archivo de eventos del aula actual.
    with open(nombre_archivo_completo, 'r') as archivo:
        # Parsea el contenido del archivo JSON.
        data = json.load(archivo)

    # Verifica que los parámetros de intervalo de fechas hayan sido
    # especificados.
    if 'start' in request.GET and 'end' in request.GET:
        # Parsea las fechas de inicio y fin indicadas.
        fecha_inicio = parse(request.GET['start']).date()
        fecha_fin = parse(request.GET['end']).date()

        # Recorre todos los eventos, en busca de aquellos que se correspondan
        # con el intervalo requerido.
        for evento in data:
            evento_inicio = parse(evento['start']).date()
            if fecha_inicio <= evento_inicio <= fecha_fin:
                # Añade el evento a la lista a retornar.
                eventos.append(evento)
    else:
        # Si no se especifica intervalo, retorna todos los eventos del aula.
        eventos = data

    # Serializa la respuesta en formato JSON. Se requiere el parámetro 'safe'
    # en falso, debido a que se retorna una lista y no un diccionario.
    return JsonResponse(eventos, safe=False)


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
