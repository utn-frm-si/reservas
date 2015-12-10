# coding=utf-8

import dj_database_url

from .base import *


DEBUG = False
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*')
DATABASES['default'] = dj_database_url.config()

# Configuración de recursos estáticos, para su uso desde Heroku.
# Fuente: https://devcenter.heroku.com/articles/django-assets
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

