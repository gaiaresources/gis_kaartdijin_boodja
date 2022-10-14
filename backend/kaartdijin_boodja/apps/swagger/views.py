"""Kaartdijin Boodja Swagger UI Django Application Views."""


# Third-Party
from django import conf
from drf_yasg import openapi
from drf_yasg import views
from rest_framework import permissions


# Swagger UI
SchemaView = views.get_schema_view(
    info=openapi.Info(
        title=conf.settings.PROJECT_TITLE,
        description=conf.settings.PROJECT_DESCRIPTION,
        default_version=conf.settings.PROJECT_VERSION,
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)
