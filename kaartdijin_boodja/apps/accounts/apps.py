"""Kaartdijin Boodja Accounts Django Application Configuration."""


# Third-Party
from django import apps


class AccountsConfig(apps.AppConfig):
    """Accounts Application Configuration."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "kaartdijin_boodja.apps.accounts"
