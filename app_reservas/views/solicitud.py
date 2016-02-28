# coding=utf-8

from django.views.generic.base import TemplateView


class SolicitudAulaView(TemplateView):
    template_name = 'app_reservas/solicitud_aula.html'


class SolicitudLaboratorioInformaticoView(TemplateView):
    template_name = 'app_reservas/solicitud_laboratorio_informatico.html'


class SolicitudMaterialMultimediaView(TemplateView):
    template_name = 'app_reservas/solicitud_material_multimedia.html'
