"""Development settings and globals."""


from os.path import join, normpath

from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## OTHER APPS CONFIGURATION
INSTALLED_APPS += (
    'django_extensions',
)
########## END OTHER APPS CONFIGURATION

########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
    'memcache_toolbar',
    'debug_toolbar_user_panel'
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'commons.profile_middleware.ProfilerMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'MEDIA_URL': MEDIA_URL,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar_user_panel.panels.UserPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'memcache_toolbar.panels.memcache.MemcachePanel',
)

########## END TOOLBAR CONFIGURATION

########## DEVSERVER CONFIGURATION
# see: https://github.com/dcramer/django-devserver

INSTALLED_APPS += (
    'devserver',
)

DEVSERVER_MODULES = (
    'commons.devserver_modules.RequestModule',
    # 'devserver.modules.sql.SQLRealTimeModule',
    # 'devserver.modules.sql.SQLSummaryModule',
    # 'devserver.modules.profile.ProfileSummaryModule',
    #
    # 'devserver.modules.ajax.AjaxDumpModule',
    # 'devserver.modules.profile.MemoryUseModule',
    # 'devserver.modules.cache.CacheSummaryModule',
    # 'devserver.modules.profile.LineProfilerModule',
)

DEVSERVER_TRUNCATE_SQL = False

#DEVSERVER_FILTER_SQL = (
#        re.compile('djkombu_\w+'),  # Filter all queries related to Celery
#)

########## DEVSERVER CONFIGURATION
