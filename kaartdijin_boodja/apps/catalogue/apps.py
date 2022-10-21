"""Kaartdijin Boodja Catalogue Django Application Configuration."""


# Third-Party
from django import apps


class CatalogueConfig(apps.AppConfig):
    """Catalogue Application Configuration."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "kaartdijin_boodja.apps.catalogue"
