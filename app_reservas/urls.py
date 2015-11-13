from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
    ),
    url(
        r'^cuerpo_(?P<num_cuerpo>[0-9]+)/$',
        views.cuerpo_detalle,
        name='cuerpo_detalle'
    ),
    url(
        r'^cuerpo_(?P<num_cuerpo>[0-9]+)/nivel_(?P<num_nivel>[0-9]+)/$',
        views.nivel_detalle,
        name='nivel_detalle'
    ),
    url(
        r'^cuerpo_(?P<num_cuerpo>[0-9]+)/nivel_(?P<num_nivel>[0-9]+)/aula_(?P<num_aula>[0-9]+)/$',
        views.aula_detalle,
        name='aula_detalle'
    ),
    url(
        r'^solicitud/aula/$',
        views.solicitud_aula,
        name='solicitud_aula'
    ),
]
