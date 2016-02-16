# -*- coding: utf-8 -*-
"""
Django developer settings

- debug mode true
- django-debug-toolbar
- django-extensions

"""

from .common import *  # noqa

# ------------------------------------------------------------------------------
# DEBUG
# ------------------------------------------------------------------------------

DEBUG = env.bool('DJANGO_DEBUG', default=True)

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG


# ------------------------------------------------------------------------------
# SECRET CONFIGURATION
# ------------------------------------------------------------------------------

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.`
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# ------------------------------------------------------------------------------
# STATIC
# ------------------------------------------------------------------------------

STATICFILES_DIRS = (
    str(ROOT_DIR.path('assets')),
)

# ------------------------------------------------------------------------------
# DJANGO DEBUG TOOLBAR
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.org/en/1.3.2/
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# ------------------------------------------------------------------------------
# DJANGO EXTENSIONS
# ------------------------------------------------------------------------------

# http://django-extensions.readthedocs.org/en/latest/installation_instructions.html
INSTALLED_APPS += ('django_extensions', )
