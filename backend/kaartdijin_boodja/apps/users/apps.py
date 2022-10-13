"""Kaartdijin Boodja Users Django Application Configuration."""


# Third-Party
from django import apps


class UsersConfig(apps.AppConfig):
    """Users Application Configuration."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "kaartdijin_boodja.apps.users"
