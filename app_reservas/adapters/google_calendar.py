from apiclient import discovery
from datetime import date, datetime, timedelta
from dateutil import parser

from reservas.settings import GOOGLE_CALENDAR_TOKEN


def obtener_eventos(calendar_id):
    service = discovery.build('calendar', 'v3', developerKey=GOOGLE_CALENDAR_TOKEN)

    now = datetime.utcnow().isoformat() + 'Z'
    yesterday = date.today() - timedelta(days=1)
    yesterday = datetime.combine(yesterday, datetime.min.time()).isoformat() + "Z"

    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=now,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    lista_eventos = []

    for event in events:
        titulo = event['summary']
        inicio = event['start'].get('dateTime', event['start'].get('date'))
        fin = event['end'].get('dateTime', event['end'].get('date'))
        inicio = parser.parse(inicio)
        fin = parser.parse(fin)
        if inicio.day == datetime.now().day:
            evento = {
                'titulo': titulo,
                'inicio': inicio,
                'fin': fin,
                'inicio_str': inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                'fin_str': fin.strftime("%Y-%m-%dT%H:%M:%S"),
            }
            lista_eventos.append(evento)

    return lista_eventos
