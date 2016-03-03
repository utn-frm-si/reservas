# coding=utf-8

from dj_database_url import config

from .production import *

DATABASES['default'] = config()
