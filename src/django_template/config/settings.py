"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/

https://github.com/pydanny/cookiecutter-django/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/config/settings/base.py
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# General
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#debug
DEBUG = True

# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "GB"

# https://docs.djangoproject.com/en/3.0/ref/settings/#language-code
LANGUAGE_CODE = "en-gb"

# https://docs.djangoproject.com/en/3.0/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/3.0/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/3.0/ref/settings/#locale-paths
# LOCALE_PATHS = os.path.join(BASE_DIR, "locale")

# https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key
SECRET_KEY = os.getenv(
    "SECRET_KEY", b"d\x07\xdf3\xfb\x90C\xeeW5\xe9\xc0\x86\x04Bi;\x1b\xfe`\x88\x1aL\xc4"
)

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Database
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Urls
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

# https://docs.djangoproject.com/en/3.0/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# Apps
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # https://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    "whitenoise.runserver_nostatic",
    #
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = []

LOCAL_APPS = [
    "apps.main",
    "apps.account",
]

# https://docs.djangoproject.com/en/3.0/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Migrations
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#migration-modules


# Authentication
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#authentication-backends
# AUTHENTICATION_BACKENDS = [
#     "django.contrib.auth.backends.ModelBackend",
# ]
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-user-model
AUTH_USER_MODEL = "account.User"
# https://docs.djangoproject.com/en/3.0/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "main:home"
# https://docs.djangoproject.com/en/3.0/ref/settings/#login-url
LOGIN_URL = "account:login"
# https://docs.djangoproject.com/en/3.0/ref/settings/#logout-redirect-url
# LOGOUT_REDIRECT_URL = "main:home"

# Passwords
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8,},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

# Middleware
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # https://whitenoise.evans.io/en/stable/django.html#enable-whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    #
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Static
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# https://docs.djangoproject.com/en/3.0/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# https://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Templates
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/3.0/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/3.0/ref/templates/api/#loader-types
            # "loaders": [
            #     "django.template.loaders.filesystem.Loader",
            #     "django.template.loaders.app_directories.Loader",
            # ],
            # https://docs.djangoproject.com/en/3.0/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Admin
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#admins
ADMINS = [("Emily", "12156026+emilyjt@users.noreply.github.com")]

# https://docs.djangoproject.com/en/3.0/ref/settings/#managers
MANAGERS = ADMINS
