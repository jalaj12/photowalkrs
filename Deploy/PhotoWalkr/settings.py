# Django settings for PhotoWalkr project.
import os.path
cwd = os.path.dirname(os.path.realpath(__file__))
import sys
sys.path.append(cwd)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

import json
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test',                      # Or path to database file if using sqlite3.
        'USER': env['DOTCLOUD_DB_MYSQL_LOGIN'],                      # Not used with sqlite3.
        'PASSWORD': env['DOTCLOUD_DB_MYSQL_PASSWORD'],                  # Not used with sqlite3.
        'HOST': env['DOTCLOUD_DB_MYSQL_HOST'],                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': int(env['DOTCLOUD_DB_MYSQL_PORT']),                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True




MEDIA_ROOT = '/home/dotcloud/data/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/dotcloud/volatile/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
                    os.path.join(os.path.dirname(__file__), 'static').replace('\\','/'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$ni2c-d35$^3d@*r+2-62^n5sbi10rir1w%u%2^#x(_4c)+8f&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'PhotoWalkr.urls'

TEMPLATE_DIRS = (
                 (cwd + '/templates'),
                 #os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'south',
    'sorl.thumbnail',
    'sorl',
    'tagging',
    'apps.profiles',
    'apps.photos',
    'apps.photowalks',
    'apps.feeds',
    'django.contrib.gis',
    'django.contrib.humanize',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

AUTH_PROFILE_MODULE = 'profiles.UserProfile'

AUTHENTICATION_BACKENDS = (
            'django.contrib.auth.backends.ModelBackend',
     )

SRID = 4326
GMAP_KEY = "ABQIAAAA496CbrflCxvduLD30wNsqhQq3tWW1UGy0rG7B4F3xzgSR63hWxSoz3WEdQlXbSF2-qEhMm4zqDCfRg"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'photowalkrs@gmail.com'
EMAIL_HOST_PASSWORD = 'photowalkrs123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True