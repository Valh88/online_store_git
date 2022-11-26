"""
Django settings for online_store project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import sys
from pathlib import Path
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env('../.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", bool)

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")
# Application definition
# docker-compose -f docker-compose.prod.yaml up -d --build create app
# docker-compose -f docker-compose.prod.yaml logs -f logi docker compost
# docker-compose exec db psql --username=django_user --dbname=django_db data db
# docker-compose -f docker-compose.prod.yml exec <container_name> python manage.py migrate
# docker-compose exec django_backend python3 manage.py migrate

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cart',
    'users',
    'products',
    'reviews',
    'taggit',
    'orders',
    'debug_toolbar',
    'rest_framework',
    'django_prometheus',
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'online_store.urls'

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
                'online_store.context_processors.catalog',
                'online_store.context_processors.cart',
                'online_store.context_processors.top_tags',

            ],
        },
    },
]

WSGI_APPLICATION = 'online_store.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

DATABASES = {
    "default": {
        # "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "ENGINE": env("SQL_ENGINE"),
        "NAME": env("SQL_DATABASE"),
        "USER": env("SQL_USER"),
        "PASSWORD": env("SQL_PASSWORD"),
        "HOST": env("SQL_HOST"),
        "PORT": env("SQL_PORT"),
    }
}
# docker-compose -f docker-compose.prod.yaml up -d --build
# docker-compose -f docker-compose.prod.yaml logs -f
# добавить ip в ALLOWED_HOSTS

# if DEBUG:
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# else:
#     EMAIL_HOST = env('EMAIL_HOST') #smtp.yandex.ru
#     EMAIL_PORT = env('EMAIL_PORT')
#     EMAIL_HOST_USER = env('EMAIL_HOST_USER')
#     EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
#     EMAIL_USE_SSL = env('EMAIL_USE_SSL')

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000", "http://localhost:1337"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#STATIC_URL = 'static/'

# STATIC_ROOT = BASE_DIR.joinpath("static")

# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static/",),
# ]

# MEDIA_ROOT = BASE_DIR.joinpath("media")

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CART_SESSION_ID = 'card'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

INTERNAL_IPS = [
    "127.0.0.1",
    'localhost',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ]
}

# REDIS_HOST = '0.0.0.0'
# REDIS_PORT = '6379'
# CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
# CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

#для докер_компост
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
#docker run -p 6379:6379 redis
#celery -A online_store worker -l info
