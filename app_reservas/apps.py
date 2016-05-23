# coding=utf-8

from django.apps import AppConfig


class ReservasConfig(AppConfig):
    name = 'app_reservas'
    verbose_name = 'Reservas'

    def ready(self):
        from .signals import recurso
