"""
Django settings for FirstD project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '-u59mw*l)lzm8k^vff9l)tx58%m)mrscvhr1)+!vz00w)++c%r'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []






PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, '../Templates'),)

MEDIA_ROOT = os.path.join(PROJECT_PATH, '/var/www/html/')

MEDIA_URL = '/var/www/html/'


STATICFILES_DIRS = (
    
    os.path.join(BASE_DIR, "static"),)

MEDIA_URL = '/var/www/html/'



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PeruCall',
    'ws4redis',


)

WEBSOCKET_URL = '/ws/'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'FirstD.urls'

WSGI_APPLICATION = 'ws4redis.django_runserver.application'

WEBSOCKET_URL = '/ws/'

WS4REDIS_EXPIRE = 3600

WS4REDIS_HEARTBEAT = '--heartbeat--'

WS4REDIS_PREFIX = 'demo'


SESSION_ENGINE = 'redis_sessions.session' # for djcelery

SESSION_REDIS_PREFIX = 'session'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'perucall',
        'USER': 'root',
        #'PASSWORD': 'd4t4B4$3p3c4ll2016*',
        'PASSWORD':'d4t4B4$3*',
        'HOST': 'xiencias.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

X_FRAME_OPTIONS = 'ACCEPT'


TEMPLATE_CONTEXT_PROCESSORS = (
    
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'ws4redis.context_processors.default',
)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'
