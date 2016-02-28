# coding=utf-8

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """
    Vista de plantilla para la página principal de la aplicación.
    """
    template_name = 'app_reservas/index.html'
