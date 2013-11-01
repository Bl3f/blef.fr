from blefpointfr.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

SECRET_KEY = os.environ.get('SECRET_KEY', 'se2*v3=&+ztpwv83a-e34clh6p1%6xc3pcqsv_j_7(zayb*p$w')

ROOT_URLCONF = 'blefpointfr.urls'

WSGI_APPLICATION = 'blefpointfr.wsgi.application'

INSTALLED_APPS += (
)