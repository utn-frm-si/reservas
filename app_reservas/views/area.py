# coding=utf-8

from django.views.generic.detail import DetailView

from app_reservas.models import Area


class AreaDetailView(DetailView):
    model = Area
    context_object_name = 'area'
