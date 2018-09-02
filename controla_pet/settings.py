"""
Django settings for controla_pet project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['systemcontrolapet.herokuapp.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'cliente',
    'core',
    'servicos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'controla_pet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'usuarios/templates',
            'cliente/templates',
            'core/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'controla_pet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')

# !!!! BANCO DOCKER !!!!
DATABASES = {
   'default': config(
        'DOCKER_DATABASE',
        cast=dburl
    ),
   'titles': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': 'titles',
   }
}

#!!!!   BANCO LOCAL MYSQL   !!!!
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DATABASE_LOCAL_NAME'),
#         'USER': config('DATABASE_LOCAL_USER'),
#         'PASSWORD': config('DATABASE_LOCAL_PASSWORD'),
#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#      },
#     'titles': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'titles',
#     }
# }

#!!!!    BANCO EM PRODUÇÃO   !!!!
#DATABASES = {
#    'default': config('AWS_DATABASE_URL', default=default_dburl, cast=dburl),
#    'titles': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'titles',
#    }
#}


DATABASE_ROUTERS = ['controla_pet.router.DatabaseAppsRouter']

DATABASE_APPS_MAPPING = {
    'core': 'titles',
    'usuarios': 'default',
    'cliente': 'default',
    'auth': 'default',
    'django': 'default',
    'admin': 'default',
    'servicos': 'default',
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'usuarios/static',
    'core/static',
    'cliente/static'
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# -----------------------------------

AUTH_USER_MODEL = 'usuarios.User'
INDEX_URL = 'index'
LOGIN_REDIRECT_URL = INDEX_URL
