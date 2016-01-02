from django.apps import AppConfig


class ReservasConfig(AppConfig):
    name = 'app_reservas'
    verbose_name = 'Reservas'

    def ready(self):
        import app_reservas.signals.recurso
