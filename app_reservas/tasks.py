import os
from celery import group, shared_task

from .models import Recurso


@shared_task(name='obtener_eventos_recursos')
def obtener_eventos_recursos():
    # Indica la ruta donde se almacenarán los archivos.
    ruta_archivos = 'media/app_reservas/eventos_recursos/'

    # Crea el directorio, en caso de que no exista.
    os.makedirs(ruta_archivos, exist_ok=True)

    # Obtiene todos los recursos existentes.
    recursos = Recurso.objects.all()

    subtareas = group(obtener_eventos_recurso_especifico.s(recurso, ruta_archivos) for recurso in recursos)
    subtareas()


@shared_task(name='obtener_eventos_recurso_especifico')
def obtener_eventos_recurso_especifico(recurso, ruta_archivos='media/app_reservas/eventos_recursos/'):
    if isinstance(recurso, Recurso):
        # Arma el nombre del archivo.
        nombre_archivo = str(recurso.id) + '.json'
        nombre_archivo_completo = ruta_archivos + nombre_archivo

        # Crea o sobrescribe el archivo del recurso actual.
        with open(nombre_archivo_completo, 'w') as archivo:
            # Escribe en el archivo los eventos del recurso, en formato JSON.
            archivo.write(recurso.get_eventos_json())
