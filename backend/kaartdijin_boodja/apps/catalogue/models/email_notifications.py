"""Kaartdijin Boodja Catalogue Django Application Email Notification Models."""


# Third-Party
from django.db import models

# Local
from . import catalogue_entries


class EmailNotificationType(models.IntegerChoices):
    """Enumeration for a Email Notification Type."""
    ON_APPROVE = 1
    ON_LOCK = 2
    BOTH = 3


class EmailNotification(models.Model):
    """Model for an Email Notification."""
    name = models.TextField()
    type = models.IntegerField(choices=EmailNotificationType.choices)  # noqa: A003
    email = models.TextField()
    catalogue_entry = models.ForeignKey(catalogue_entries.CatalogueEntry, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.name}"
