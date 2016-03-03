# coding=utf-8

import csv
from io import TextIOWrapper

from django.shortcuts import render

from .models import Usuario


def index(request):
    return render(
        request,
        'app_facturacion/spreadsheet.html'
    )

def csv_processing(request):
    if request.method == 'GET':
        return render(
            request,
            'app_facturacion/csv_upload.html'
        )
    if request.method == 'POST':
        # Obtiene el archivo subido.
        f = TextIOWrapper(request.FILES['file'].file, encoding='latin-1')
        # Crea un lector para el archivo CSV, con delimitadores ';'.
        reader = csv.DictReader(f, delimiter=';')

        # Crea las variables a retornar.
        resumen = {}
        lineas_no_reconocidas = []

        # Obtiene todos los usuarios del sistema.
        usuarios = Usuario.objects.all()

        # Recorre cada registro del archivo CSV.
        for row in reader:
            # Obtiene todos los campos.
            numero_linea = row['BILL_NUMBER']
            concepto = row['DESCRIPCION_CONCEPTO']
            cantidad = row['CANTIDAD']
            monto_neto = row['MONTO_NETO']
            monto_impuesto = row['MONTO_IMPUESTOS']
            monto_total = row['MONTO_NETO']

            # Omite la línea, si no presenta número de línea.
            if numero_linea == '':
                continue

            # Convierte los campos decimales, reemplazando ',' por '.' y
            # convirtiéndolo a flotante.
            cantidad = float(cantidad.replace(',', '.'))
            monto_neto = float(monto_neto.replace(',', '.'))
            monto_impuestos = float(monto_impuesto.replace(',', '.'))
            monto_total = float(monto_total.replace(',', '.'))

            # Si la línea ya está presente en el resumen, añade la información
            # del registro.
            if numero_linea in resumen:
                resumen[numero_linea]['monto_total'] += monto_total
                resumen[numero_linea]['conceptos'].append({
                    'descripcion': concepto,
                    'cantidad': cantidad,
                    'monto_neto': monto_neto,
                    'monto_impuestos': monto_impuestos,
                    'monto_total': monto_total,
                })
            # Sino, añade la línea al resumen.
            else:
                usuario_asociado = None
                for usuario in usuarios:
                    lineas_usuario = usuario.lineatelefonica_set.all()
                    for linea_usuario in lineas_usuario:
                        if str(linea_usuario.numero) == numero_linea:
                            usuario_asociado = usuario
                            break
                    if usuario_asociado is not None:
                        break

                if usuario_asociado is None:
                    lineas_no_reconocidas.append(numero_linea)
                else:
                    linea = {
                        'usuario': str(usuario_asociado),
                        'monto_total': monto_total,
                        'conceptos': [{
                            'descripcion': concepto,
                            'cantidad': cantidad,
                            'monto_neto': monto_neto,
                            'monto_impuestos': monto_impuestos,
                            'monto_total': monto_total,
                        }],
                    }
                    resumen[numero_linea] = linea
        return render(
            request,
            'app_facturacion/csv_read.html',
            context={
                'resumen': resumen,
                'lineas_no_reconocidas': lineas_no_reconocidas,
            }
        )
