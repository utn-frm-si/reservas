# coding=utf-8

from django.conf.urls import url

from .views import (
    AliVideoconferenciasDetailView,
    AreaDetailView,
    AulaDetailView,
    CuerpoDetailView,
    IndexView,
    LaboratorioDetailView,
    LaboratorioInformaticoDetailView,
    LaboratorioInformaticoListView,
    NivelDetailView,
    recurso_eventos_json,
    RecursoAliDetailView,
    SolicitudAliReclamosSugerencias,
    SolicitudAulaView,
    SolicitudInstalacionSoftwareView,
    SolicitudLaboratorioInformaticoView,
    SolicitudMaterialMultimediaView,
    TipoLaboratorioDetailView,
    TipoRecursoAliDetailView,
    TvCuerposListView,
    TvVisorCuerposDetailView,
    TvVisorDetailView,
)


urlpatterns = [
    url(
        r'^$',
        IndexView.as_view(),
        name='index'
    ),
    url(
        r'^cuerpo/(?P<numero>\d+)/$',
        CuerpoDetailView.as_view(),
        name='cuerpo_detalle'
    ),
    url(
        r'^cuerpo/(?P<numero_cuerpo>\d+)/nivel/(?P<numero_nivel>-?\d+)/$',
        NivelDetailView.as_view(),
        name='nivel_detalle'
    ),
    url(
        r'^aula/(?P<pk>\d+)/$',
        AulaDetailView.as_view(),
        name='aula_detalle'
    ),
    url(
        r'^area/(?P<slug>[-\w]+)/$',
        AreaDetailView.as_view(),
        name='area_detalle'
    ),
    url(
        r'^recurso/(?P<pk>\d+)/eventos/$',
        recurso_eventos_json,
        name='recurso_eventos_json'
    ),
    url(
        r'^ali/videoconferencias/$',
        AliVideoconferenciasDetailView.as_view(),
        name='ali_videoconferencias_detalle'
    ),
    url(
        r'^laboratorios/informatica/$',
        LaboratorioInformaticoListView.as_view(),
        name='laboratorio_informatico_listado'
    ),
    url(
        r'^laboratorio/informatica/(?P<alias>[A-Za-z0-9]+)/$',
        LaboratorioInformaticoDetailView.as_view(),
        name='laboratorio_informatico_detalle'
    ),
    url(
        r'^laboratorios/(?P<slug>[-\w]+)/$',
        TipoLaboratorioDetailView.as_view(),
        name='tipo_laboratorio_detalle'
    ),
    url(
        r'^laboratorio/(?P<tipo>[A-Za-z0-9]+)/(?P<alias>[A-Za-z0-9]+)/$',
        LaboratorioDetailView.as_view(),
        name='laboratorio_detalle'
    ),
    url(
        r'^ali/(?P<slug>[-\w]+)/$',
        TipoRecursoAliDetailView.as_view(),
        name='tipo_recurso_ali_detalle'
    ),
    url(
        r'^ali/(?P<tipo>[-\w]+)/(?P<identificador>[A-Za-z0-9_-]+)/$',
        RecursoAliDetailView.as_view(),
        name='recurso_ali_detalle'
    ),
    url(
        r'^solicitud/ali/reclamos_sugerencias/$',
        SolicitudAliReclamosSugerencias.as_view(),
        name='solicitud_ali_reclamos_sugerencias'
    ),
    url(
        r'^solicitud/aula/$',
        SolicitudAulaView.as_view(),
        name='solicitud_aula'
    ),
    url(
        r'^solicitud/instalacion_software/$',
        SolicitudInstalacionSoftwareView.as_view(),
        name='solicitud_instalacion_software'
    ),
    url(
        r'^solicitud/laboratorio/informatica/$',
        SolicitudLaboratorioInformaticoView.as_view(),
        name='solicitud_laboratorio_informatico'
    ),
    url(
        r'^solicitud/material_multimedia/$',
        SolicitudMaterialMultimediaView.as_view(),
        name='solicitud_material_multimedia'
    ),
    url(
        r'^tv/cuerpos/$',
        TvCuerposListView.as_view(),
        name='tv_cuerpos'
    ),
    url(
        r'^tv/visor/(?P<slug>[-\w]+)/$',
        TvVisorDetailView.as_view(),
        name='tv_visor'
    ),
    url(
        r'^tv/visor/(?P<slug>[-\w]+)/cuerpos/$',
        TvVisorCuerposDetailView.as_view(),
        name='tv_visor_cuerpos'
    ),

    # TODO: Eliminar. Vistas obsoletas debido a las vistas de VisorTv. Sólo se
    # mantienen para compatibilidad con los visores que funcionan actualmente.
    url(
        r'^tv/bedelia/(?P<slug>[-\w]+)/$',
        TvVisorDetailView.as_view(),
        name='tv_bedelia'
    ),
    url(
        r'^tv/bedelia/(?P<slug>[-\w]+)/cuerpos/$',
        TvVisorCuerposDetailView.as_view(),
        name='tv_bedelia_cuerpos'
    ),
]
