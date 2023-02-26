### DEVELOPMENT SETTINGS ###

from .base import *

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'django-insecure-*y^w7d_^t+-fht#p%6c^3!x+3+il#aewwz_mng92lez8yu0w)$'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += []

MIDDLEWARE = [] + MIDDLEWARE
