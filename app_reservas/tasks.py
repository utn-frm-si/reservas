# coding=utf-8

import os
from celery import (
    group,
    shared_task,
)
import json

from .models import Recurso


@shared_task(name='obtener_eventos_recursos')
def obtener_eventos_recursos():
    # Indica la ruta donde se almacenarán los archivos.
    ruta_archivos = 'media/app_reservas/eventos_recursos/'

    # Crea el directorio, en caso de que no exista.
    os.makedirs(ruta_archivos, exist_ok=True)

    # Obtiene todos los recursos existentes.
    recursos = Recurso.objects.all()

    subtareas = group(obtener_eventos_recurso_especifico.s(recurso, ruta_archivos)
                      for recurso in recursos)
    subtareas()


@shared_task(name='obtener_eventos_recurso_especifico')
def obtener_eventos_recurso_especifico(recurso,
                                       ruta_archivos='media/app_reservas/eventos_recursos/'):
    # Verifica que el objeto recibido sea una instancia de Recurso (o alguna de sus subclases).
    if not isinstance(recurso, Recurso):
        return

    # Arma el nombre del archivo.
    nombre_archivo = str(recurso.id) + '.json'
    nombre_archivo_completo = ruta_archivos + nombre_archivo

    # Obtiene los eventos del recurso en formato JSON.
    eventos = recurso.get_eventos_json()

    # Verifica que se hayan obtenido eventos, ya que en caso de no obtenerse por algún problema de
    # conexión, no debe sobrescribirse el archivo de eventos del recurso.
    if json.loads(eventos):
        # Crea o sobrescribe el archivo del recurso actual.
        with open(nombre_archivo_completo, 'w') as archivo:
            # Escribe en el archivo los eventos del recurso, en formato JSON.
            archivo.write(eventos)
