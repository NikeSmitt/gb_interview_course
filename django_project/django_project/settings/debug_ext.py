from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^36j(2az+n+zbb**l!6bi8o7oo#h-8=6f*p2w_&wtw8ivqa$@f'
DEBUG = True
ALLOWED_HOSTS = ['*']
SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django-project',
        'USER': 'user',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
