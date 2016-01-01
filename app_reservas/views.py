# coding=utf-8

import json
from datetime import date
from dateutil.parser import parse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Area, Aula, Cuerpo, LaboratorioInformatico, Nivel, Recurso


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


def laboratorio_informatico_detalle(request, alias_laboratorio):
    # Obtiene el laboratorio informático por su alias.
    laboratorio = get_object_or_404(LaboratorioInformatico, alias=alias_laboratorio)
    return render(
        request,
        'app_reservas/laboratorio_informatico_detalle.html',
        {
            'laboratorio': laboratorio,
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


def recurso_eventos_json(request, recurso_id):
    # Indica la ruta donde se almacenan los archivos JSON de eventos de recursos.
    ruta_archivos = 'media/app_reservas/eventos_recursos/'

    # Obtiene el recurso especificado.
    recurso = get_object_or_404(Recurso, id=recurso_id)

    # Arma el nombre del archivo.
    nombre_archivo = str(recurso.id) + '.json'
    nombre_archivo_completo = ruta_archivos + nombre_archivo

    # Inicializa la lista de eventos a retornar.
    eventos = []

    # Lee el archivo de eventos del recurso actual.
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
