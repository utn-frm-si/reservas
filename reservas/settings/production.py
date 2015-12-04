# coding=utf-8

import dj_database_url

from .base import *


DEBUG = False
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*')
DATABASES['default'] = dj_database_url.config()
