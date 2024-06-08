"""
Django settings for ResearchTracker project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

from celery.schedules import crontab
from django.contrib import staticfiles

# from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(-$_3^gllkqp59zsoexa%oy!5*cp5l@-#r!uk($ov_j2dv--(2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.syndication',
    'rest_framework',
    'authentication',
    'projects',
    'publications',
    'reports',
    'notifications',
    'fundings',
    "dashboard.apps.DashboardConfig",
    "userprofile.apps.UserprofileConfig",
    "summarizer.apps.SummarizerConfig",
    "api.apps.ApiConfig",
    "feeds.apps.FeedsConfig",
    "contact.apps.ContactConfig",
    "home.apps.HomeConfig",
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

ROOT_URLCONF = 'ResearchTracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'ResearchTracker.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'yjndwnsp_researchtracker',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',  # Hôte fourni par PlanetHoster
#         'PORT': '3306',
#     }
# }

#Railway base de données distante
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'railway',
#         'USER': 'root',
#         'PASSWORD': 'jCpyeOWhXiDJZKJdRlgYZgIsrzpFsqiv',
#         'HOST': 'monorail.proxy.rlwy.net',
#         'PORT': '50369',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'yjndwnsp_researchtracker',
#         'USER': 'yjndwnsp_root',
#         'PASSWORD': 'Garcia66240',
#         'HOST': 'node109-eu.n0c.com', ici localhost  # Hôte fourni par PlanetHoster
#         'PORT': '3306',
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ajoutez ce paramètre pour inclure les répertoires statiques de chaque application
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'authentication.CustomUser'


LOGIN_URL = 'login/'  # Nom de l'URL pour la page de connexion
LOGIN_REDIRECT_URL = '/'  # Redirection après une connexion réussie
LOGOUT_REDIRECT_URL = '/'  # Redirection après une déconnexion réussie


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),  # Utilisez un chemin valide
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

CELERY_BROKER_URL = 'redis://:qLg8E8JBYoNxLpnGGlwVe8hJ2pXTyulj@redis-16622.c304.europe-west1-2.gce.redns.redis-cloud.com:16622/0'
CELERY_RESULT_BACKEND = 'redis://:qLg8E8JBYoNxLpnGGlwVe8hJ2pXTyulj@redis-16622.c304.europe-west1-2.gce.redns.redis-cloud.com:16622/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_IMPORTS = [
    'ResearchTracker.tasks',
]

CELERY_BEAT_SCHEDULE = {
    'update-feeds-every-hour': {
        'task': 'ResearchTracker.tasks.update_all_feeds',
        'schedule': crontab(minute='*/30'),  # Exécute toutes les 30 minutes
    },
}

# load_dotenv()
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
