from apiclient import discovery
from datetime import datetime
from dateutil import parser

from reservas.settings import GOOGLE_CALENDAR_TOKEN


def crear_servicio():
    return discovery.build('calendar', 'v3', developerKey=GOOGLE_CALENDAR_TOKEN)


def get_fecha_actual():
    now = datetime.utcnow().isoformat() + 'Z'
    return now


def generar_lista_eventos(eventos):
    lista_eventos = []

    for evento in eventos:
        titulo = evento['summary']
        inicio = evento['start'].get('dateTime', evento['start'].get('date'))
        fin = evento['end'].get('dateTime', evento['end'].get('date'))
        inicio = parser.parse(inicio)
        fin = parser.parse(fin)

        evento = {
            'titulo': titulo,
            'inicio': inicio,
            'fin': fin,
            'inicio_str': inicio.strftime("%Y-%m-%dT%H:%M:%S"),
            'fin_str': fin.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        lista_eventos.append(evento)

    return lista_eventos


def obtener_eventos(calendar_id):
    service = crear_servicio()

    events_result = service.events().list(
        calendarId=calendar_id,
        maxResults=2500,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    eventos = events_result.get('items', [])
    return generar_lista_eventos(eventos)


def obtener_eventos_dia(calendar_id):
    service = crear_servicio()

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=get_fecha_actual(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    eventos = events_result.get('items', [])
    return generar_lista_eventos(eventos)
