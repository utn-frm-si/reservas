# coding=utf-8

from django.views.generic.detail import DetailView

from app_reservas.models import Aula


class AulaDetailView(DetailView):
    model = Aula
    context_object_name = 'aula'
