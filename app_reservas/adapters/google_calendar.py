# coding=utf-8

from apiclient import discovery
from datetime import datetime
from dateutil import parser
from httplib2 import ServerNotFoundError

from reservas.settings.base import GOOGLE_CALENDAR_TOKEN


def crear_servicio():
    """Construye un servicio para comunicarse con la API de Google Calendar.

    Returns
    -------
    object
        Objeto que proporciona el servicio de comunicación con la API de Google Calendar.
    """
    return discovery.build('calendar', 'v3', developerKey=GOOGLE_CALENDAR_TOKEN)


def generar_lista_eventos(calendar_id, limite_anio_siguiente=True):
    """Genera el listado de eventos de un calendario específico de Google Calendar.

    Retorna el listado de eventos de un calendario específico de Google Calendar, con la
    información requerida por la aplicación. En caso de que se produzca algún problema de conexión
    a Google Calendar, no se retorna ningún evento.

    Parameters
    ----------
    calendar_id : str
        ID de calendario de Google Calendar.
    limite_anio_siguiente : bool, optional
        Variable que especifica que los eventos a obtener comprendan únicamente a aquellos del año
        actual y el año próximo. En caso de ser falso, se obtienen todos los eventos del
        calendario, sin considerar la fecha de los mismos. Por defecto, es verdadero.

    Returns
    -------
    list of dicts
        Lista de eventos, organizados como diccionarios.
    """
    lista_eventos = []

    # Obtiene de Google Calendar los eventos del calendario.
    eventos = obtener_eventos(calendar_id, limite_anio_siguiente)

    for evento in eventos:
        inicio = parser.parse(
            evento['start'].get(
                'dateTime',
                evento['start'].get('date')
            )
        )
        fin = parser.parse(
            evento['end'].get(
                'dateTime',
                evento['end'].get('date')
            )
        )

        lista_eventos.append(
            {
                'titulo': evento.get('summary', u'Evento sin título'),
                'inicio': inicio,
                'fin': fin,
                'inicio_str': inicio.strftime("%Y-%m-%dT%H:%M:%S"),
                'fin_str': fin.strftime("%Y-%m-%dT%H:%M:%S"),
            }
        )

    return lista_eventos


def obtener_eventos(calendar_id, limite_anio_siguiente=True):
    """Obtiene de Google Calendar los eventos de un calendario específico.

    Retorna los eventos de un calendario específico, solicitados a la API de Google Calendar. En
    caso de que se produzca algún problema de conexión a Google Calendar, no se retorna ningún
    evento.

    Parameters
    ----------
    calendar_id : str
        ID de calendario de Google Calendar.
    limite_anio_siguiente : bool, optional
        Variable que especifica que los eventos a obtener comprendan únicamente a aquellos del año
        actual y el año próximo. En caso de ser falso, se obtienen todos los eventos del
        calendario, sin considerar la fecha de los mismos. Por defecto, es verdadero.

    Returns
    -------
    list of dicts
        Lista de eventos, organizados como diccionarios.
    """
    service = crear_servicio()

    primer_dia_anio_actual = None
    primer_dia_anio_subsiguiente = None
    if limite_anio_siguiente:
        # Obtiene únicamente los eventos del año actual y el siguiente.
        primer_dia_anio_actual = datetime(
            datetime.today().year,
            1,
            1,
        ).isoformat('T') + 'Z'
        primer_dia_anio_subsiguiente = datetime(
            datetime.today().year + 2,
            1,
            1,
        ).isoformat('T') + 'Z'

    eventos = []
    page_token = None

    while True:
        try:
            # Realiza la petición de eventos del calendario a Google Calendar.
            events_result = service.events().list(
                calendarId=calendar_id,
                maxResults=2500,
                singleEvents=True,
                timeMin=primer_dia_anio_actual,
                timeMax=primer_dia_anio_subsiguiente,
                pageToken=page_token,
                orderBy='startTime'
            ).execute()
        except ServerNotFoundError:
            # En caso de problemas de conexión a Google Calendar, no se retorna ningún evento.
            eventos = []
            break

        # Añade los eventos obtenidos de la petición al listado de eventos.
        eventos.extend(events_result.get('items', []))

        # Se recupera el token de página retornado por la petición a Google Calendar. Este token,
        # en caso de estar especificado, indica que se debe realizar otra petición para obtener una
        # nueva página de eventos para el calendario.
        page_token = events_result.get('nextPageToken')
        # Si no se obtuvo token de página, se ha finalizado con la obtención de eventos.
        if not page_token:
            break

    return eventos
