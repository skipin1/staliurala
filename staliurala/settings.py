from os.path import dirname, join

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = dirname(dirname(__file__))

PROJECT_DIR = dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '##q=9e&ql51z%0elb4ax4pfw-o8qn2suvj!iou0gfm)y8(9cmo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [] if DEBUG else ['*']


# Application definition

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_ADMIN_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
)

THIRD_PARTY_APPS = (
    'django_cleanup',
    'django_summernote',
)

USER_APPS = (
    'partners',
    'catalog',
    'site_settings',
    'tools',
)

DEBUG_APPS = (
    'debug_toolbar',
)

INSTALLED_APPS = THIRD_PARTY_ADMIN_APPS + DJANGO_APPS + USER_APPS + THIRD_PARTY_APPS
if DEBUG: INSTALLED_APPS += DEBUG_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'staliurala.urls'

WSGI_APPLICATION = 'staliurala.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    join(PROJECT_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')


TEMPLATE_DIRS = (
    join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

# DJANGO-ADMIN-TOOLS SETTINGS
ADMIN_TOOLS_MENU = 'staliurala.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'staliurala.index_dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'staliurala.app_dashboard.CustomAppIndexDashboard'


# DEBUG-TOOLBAR CONFIGURE
DEBUG_TOOLBAR_PATCH_SETTINGS = False
if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = True
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]


# SUMMERNOTE SETTINGS
SUMMERNOTE_CONFIG = {
    'styleWithTags': True,
    'lang': 'ru-RU',
    'width': '1014',
    'height': '480',
    'airMode': 'True',
}