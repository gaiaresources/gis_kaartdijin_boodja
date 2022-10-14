"""Kaartdijin Boodja Catalogue Django Application Web Notification Models."""


# Third-Party
from django.db import models

# Local
from . import catalogue_entries


class WebhookNotificationType(models.IntegerChoices):
    """Enumeration for a Webhook Notification Type."""
    ON_APPROVE = 1
    ON_LOCK = 2
    BOTH = 3


class WebhookNotification(models.Model):
    """Model for a Webhook Notification."""
    name = models.TextField()
    type = models.IntegerField(choices=WebhookNotificationType.choices)  # noqa: A003
    url = models.URLField()
    catalogue_entry = models.ForeignKey(
        catalogue_entries.CatalogueEntry,
        related_name="webhook_notifications",
        on_delete=models.CASCADE,
    )

    class Meta:
        """Webhook Notification Model Metadata."""
        verbose_name = "Webhook Notification"
        verbose_name_plural = "Webhook Notifications"

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.name}"
