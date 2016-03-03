from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
    ),
    url(
        r'^csv$',
        views.csv_processing,
        name='csv_processing'
    ),
]
