"""Django settings for the Kaartdijin Boodja project.

Generated by `django-admin startproject` using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


# Standard
import os
import pathlib
import platform

# Third-Party
import decouple
import dj_database_url


# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / "staticfiles"

# Project specific settings
PROJECT_TITLE = "Kaartdijin Boodja"
PROJECT_DESCRIPTION = "DBCA CDDP Catalogue and Publishing Django REST API"
PROJECT_VERSION = "v1"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: don't allow all hosts in production!
SECRET_KEY = decouple.config("SECRET_KEY")
DEBUG = decouple.config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = decouple.config("ALLOWED_HOSTS", default=["*"] if DEBUG else [])

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "webtemplate_dbca",
    "govapp",
    "govapp.apps.accounts",
    "govapp.apps.catalogue",
    "govapp.apps.emails",
    "govapp.apps.logs",
    "govapp.apps.publisher",
    "govapp.apps.swagger",
    "rest_framework",
    "drf_spectacular",
    "django_filters",
    "reversion",
    "django_cron",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "dbca_utils.middleware.SSOLoginMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "govapp.middleware.CacheControl",
]
ROOT_URLCONF = "govapp.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "govapp/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "govapp.context_processors.variables",
            ],
        },
    },
]
WSGI_APPLICATION = "govapp.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": decouple.config("DATABASE_URL", cast=dj_database_url.parse, default="sqlite://memory"),
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "govapp/static"  # Look for static files in the frontend
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Caching settings
# https://docs.djangoproject.com/en/3.2/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cache",
    }
}

# DBCA Template Settings
# https://github.com/dbca-wa/django-base-template/blob/main/govapp/settings.py
DEV_APP_BUILD_URL = decouple.config("DEV_APP_BUILD_URL", default=None)
ENABLE_DJANGO_LOGIN = decouple.config("ENABLE_DJANGO_LOGIN", default=False, cast=bool)
LEDGER_TEMPLATE = "bootstrap5"
GIT_COMMIT_HASH = os.popen(f"cd {BASE_DIR}; git log -1 --format=%H").read()  # noqa: S605
GIT_COMMIT_DATE = os.popen(f"cd {BASE_DIR}; git log -1 --format=%cd").read()  # noqa: S605
VERSION_NO = "2.00"

# Django REST Framework Settings
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

# DRF Spectacular Settings
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
SPECTACULAR_SETTINGS = {
    "TITLE": PROJECT_TITLE,
    "DESCRIPTION": PROJECT_DESCRIPTION,
    "VERSION": PROJECT_VERSION,
    "SERVE_INCLUDE_SCHEMA": True,
    "POSTPROCESSING_HOOKS": [],
    "COMPONENT_SPLIT_REQUEST": True,
}

# Logging
# https://docs.djangoproject.com/en/3.2/topics/logging/
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# Sharepoint Settings
SHAREPOINT_URL = decouple.config("SHAREPOINT_URL", default="https://dpaw.sharepoint.com/teams/KaartdijinBoodja-dev")
SHAREPOINT_USERNAME = decouple.config("SHAREPOINT_USERNAME", default=None)  # TODO: Credentials?
SHAREPOINT_PASSWORD = decouple.config("SHAREPOINT_PASSWORD", default=None)  # TODO: Credentials?
SHAREPOINT_LIST = decouple.config("SHAREPOINT_LIST", default="Shared Documents")
SHAREPOINT_STAGING_AREA = decouple.config("SHAREPOINT_STAGING_AREA", default="KaartdijinBoodjaLayerSubmissionStagingArea")  # noqa: E501
SHAREPOINT_ARCHIVE_AREA = decouple.config("SHAREPOINT_ARCHIVE_AREA", default="KaartdijinBoodjaLayerSubmissionArchive")

# Email
DISABLE_EMAIL = decouple.config("DISABLE_EMAIL", default=False, cast=bool)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = decouple.config("EMAIL_HOST", default="smtp.lan.fyi")
EMAIL_PORT = decouple.config("EMAIL_PORT", default=25, cast=int)
DEFAULT_FROM_EMAIL = "no-reply@dbca.wa.gov.au"

# Group Settings
# This must match what is in the database
GROUP_ADMINISTRATOR_ID = 1
GROUP_ADMINISTRATOR_NAME = "Administrators"
GROUP_CATALOGUE_EDITOR_ID = 2
GROUP_CATALOGUE_EDITOR_NAME = "Catalogue Editors"

# Cron Jobs
# https://django-cron.readthedocs.io/en/latest/installation.html
# https://django-cron.readthedocs.io/en/latest/configuration.html
CRON_SCANNER_CLASS = "govapp.apps.catalogue.cron.ScannerCronJob"
CRON_SCANNER_PERIOD_MINS = 5  # Run every 5 minutes
CRON_CLASSES = [
    CRON_SCANNER_CLASS,
]

# GeoServer Settings
GEOSERVER_URL = decouple.config("GEOSERVER_URL", default="http://127.0.0.1:8600/geoserver")
GEOSERVER_USERNAME = decouple.config("GEOSERVER_USERNAME", default="admin")
GEOSERVER_PASSWORD = decouple.config("GEOSERVER_PASSWORD", default="geoserver")
GEOSERVER_DEFAULT_WORKSPACE_ID = 1  # Must match database

# Temporary Fix for ARM Architecture
if platform.machine() == "arm64":
    GDAL_LIBRARY_PATH = "/opt/homebrew/opt/gdal/lib/libgdal.dylib"
    GEOS_LIBRARY_PATH = "/opt/homebrew/opt/geos/lib/libgeos_c.dylib"
