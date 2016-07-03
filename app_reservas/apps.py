# coding=utf-8

from django.apps import AppConfig


class ReservasConfig(AppConfig):
    name = 'app_reservas'
    verbose_name = 'Reservas'

    # Importa todas las tareas de Celery existentes, para hacer uso de las
    # mismas dentro de toda la aplicación.
    from . import tasks
