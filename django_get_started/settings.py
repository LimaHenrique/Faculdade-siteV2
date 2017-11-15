 -"""
 -Django settings for django_get_started project.
 -"""
 +
  from os import path
  import os
  mysqlconnstr = os.environ['MYSQLCONNSTR_localdb']
      }
  }
  
 -# Local time zone for this installation. Choices can be found here:
 -# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
 -# although not all choices may be available on all operating systems.
 -# On Unix systems, a value of None will cause Django to use the same
 -# timezone as the operating system.
 -# If running in a Windows environment this must be set to the same as your
 -# system time zone.
  TIME_ZONE = 'America/Sao_Paulo'
  
 -# Language code for this installation. All choices can be found here:
 -# http://www.i18nguy.com/unicode/language-identifiers.html
  LANGUAGE_CODE = 'pt-br'
  
 -# If you set this to False, Django will make some optimizations so as not
 -# to load the internationalization machinery.
  USE_I18N = True
 -
 -# If you set this to False, Django will not format dates, numbers and
 -# calendars according to the current locale.
  USE_L10N = True
  
 -# If you set this to False, Django will not use timezone-aware datetimes.
  USE_TZ = True
  
  STATIC_URL = '/static/'
 -
 -# Make this unique, and don't share it with anybody.
  SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'
  
 -# List of callables that know how to import templates from various sources.
  TEMPLATE_LOADERS = (
      'django.template.loaders.filesystem.Loader',
      'django.template.loaders.app_directories.Loader',
  ROOT_URLCONF = 'django_get_started.urls'
  
 -# Python dotted path to the WSGI application used by Django's runserver.
  WSGI_APPLICATION = 'django_get_started.wsgi.application'
  
 -TEMPLATE_DIRS = (
 -    # Put strings here, like "/home/html/django_templates" or
 -    # "C:/www/django/templates".
 -    # Always use forward slashes, even on Windows.
 -    # Don't forget to use absolute paths, not relative paths.
 -)
 -
  INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
  ]
 -# A sample logging configuration. The only tangible logging
 -# performed by this configuration is to send an email to
 -# the site admins on every HTTP 500 error when DEBUG=False.
 -# See http://docs.djangoproject.com/en/dev/topics/logging for
 -# more details on how to customize your logging configuration.
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      }
  }
  
 -# Specify the default test runner.
  TEST_RUNNER = 'django.test.runner.DiscoverRunner'
