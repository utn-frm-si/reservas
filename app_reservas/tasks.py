import os
from celery import group, shared_task

from .models import Aula


@shared_task(name='obtener_eventos_recursos')
def obtener_eventos_recursos():
    # Indica la ruta donde se almacenarán los archivos.
    ruta_archivos = 'media/app_reservas/eventos_aulas/'

    # Crea el directorio, en caso de que no exista.
    os.makedirs(ruta_archivos, exist_ok=True)

    # Obtiene todas las aulas del sistema.
    aulas = Aula.objects.all()

    subtareas = group(obtener_eventos_recurso_especifico.s(aula, ruta_archivos) for aula in aulas)
    subtareas()


@shared_task(name='obtener_eventos_recurso_especifico')
def obtener_eventos_recurso_especifico(aula, ruta_archivos):
    if isinstance(aula, Aula):
        # Arma el nombre del archivo.
        nombre_archivo = str(aula.id) + '.json'
        nombre_archivo_completo = ruta_archivos + nombre_archivo

        # Crea o sobrescribe el archivo del aula actual.
        with open(nombre_archivo_completo, 'w') as archivo:
            # Escribe en el archivo los eventos del aula, en formato JSON.
            archivo.write(aula.get_eventos_json())
