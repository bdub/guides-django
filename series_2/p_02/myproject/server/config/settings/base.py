# -*- coding: utf-8 -*-
"""
Django settings for {{ cookiecutter.repo_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

import environ

ROOT_DIR = environ.Path(__file__) - 4  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('server')


env = environ.Env()

# ------------------------------------------------------------------------------
# SECRET CONFIGURATION
# ------------------------------------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# ------------------------------------------------------------------------------
# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    # wagtail dependencies
    'compressor',
    'taggit',
    'modelcluster',

    # wagtail
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailsites',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
)

LOCAL_APPS = (
    'apps.wagtail.pages',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ------------------------------------------------------------------------------
# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Wagtail Middleware
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]


# ------------------------------------------------------------------------------
# DEBUG
# ------------------------------------------------------------------------------

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# ------------------------------------------------------------------------------
# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': env.db("DATABASE_URL", default="postgres://dev:dev@localhost/myproject")
}

# ------------------------------------------------------------------------------
# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ALLOWED_HOSTS = []

# ------------------------------------------------------------------------------
# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR('templates'))
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

# ------------------------------------------------------------------------------
# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

STATIC_ROOT = str(ROOT_DIR.path('server/staticfiles'))

# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# ------------------------------------------------------------------------------
# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(ROOT_DIR('server/media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# ------------------------------------------------------------------------------
# URL Configuration
# ------------------------------------------------------------------------------

ROOT_URLCONF = 'config.urls'


# ------------------------------------------------------------------------------
# OTHER Configuration
# ------------------------------------------------------------------------------

ADMINS = (
    ("""{{cookiecutter.author_name}}""", '{{cookiecutter.email}}'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


WSGI_APPLICATION = 'config.wsgi.application'

# ------------------------------------------------------------------------------
# LOGGIN INFORMATION
# ------------------------------------------------------------------------------

LOG_DIR = env("LOG_DIR", default=str(ROOT_DIR('logs')))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(levelname)s] -- %(asctime)s -- %(module)s:%(lineno)s ___ %(message)s >>> "
                      "{ process: %(process)d | thread: %(thread)d }",
            'datefmt': "%b %e, %I:%M:%S %p"
        },
        'simple': {
            'format': '[%(levelname)s] -- %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', ],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + '/server/django.log',
            'maxBytes': 20 * 1024 * 1024,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file_error', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['file_error', 'console', 'mail_admins', ],
            'propagate': True
        },
        'development': {
            'handlers': ['console', ],
            'level': 'DEBUG',
            'propagate': True
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# ------------------------------------------------------------------------------
# WAGTAIL SETTINGS
# ------------------------------------------------------------------------------

WAGTAIL_SITE_NAME = 'myproject'
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = True
TAGGIT_CASE_INSENSITIVE = True
