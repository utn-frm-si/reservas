# coding=utf-8

from django.db.models.signals import post_save

from ..models import Recurso
from ..tasks import obtener_eventos_recurso_especifico


def obtener_eventos(sender, instance, created, **kwargs):
    if created:
        obtener_eventos_recurso_especifico.delay(instance)

# Conecta la clase 'Recurso' y todas sus subclases a la señal 'post_save'.
# Esto se realiza ya que, al conectar sólo la clase 'Recurso', la señal no es
# enviada cuando se crea una instancia de alguna de sus subclases, debido a que
# no es propagada.
post_save.connect(obtener_eventos, Recurso)
for subclass in Recurso.__subclasses__():
    post_save.connect(obtener_eventos, subclass)
