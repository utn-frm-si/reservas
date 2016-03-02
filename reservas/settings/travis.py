# coding=utf-8

from .production import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_reservas',
        'USER': 'postgres',
        'HOST': 'localhost',
    }
}
