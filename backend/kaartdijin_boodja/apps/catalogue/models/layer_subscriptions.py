"""Kaartdijin Boodja Catalogue Django Application Layer Subscription Models."""


# Third-Party
from django.db import models


class LayerSubscriptionStatus(models.IntegerChoices):
    """Enumeration for a Layer Subscription Status."""
    ACTIVE = 1
    DISABLED = 2


class LayerSubscription(models.Model):
    """Model for a Layer Subscription."""
    name = models.TextField()
    url = models.URLField()
    frequency = models.DurationField()
    status = models.IntegerField(choices=LayerSubscriptionStatus.choices, default=LayerSubscriptionStatus.ACTIVE)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.name}"
