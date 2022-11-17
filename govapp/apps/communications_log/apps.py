"""Kaartdijin Boodja Communications Log Django Application Configuration."""


# Third-Party
from django import apps


class CommunicationsLogConfig(apps.AppConfig):
    """Communications Log Application Configuration."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "govapp.apps.communications_log"
