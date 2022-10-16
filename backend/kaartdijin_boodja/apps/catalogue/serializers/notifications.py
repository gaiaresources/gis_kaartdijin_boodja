"""Kaartdijin Boodja Catalogue Django Serializers."""


# Third-Party
from rest_framework import serializers

# Local
from .. import models


class EmailNotificationSerializer(serializers.ModelSerializer):
    """Email Notification Model Serializer."""
    type = serializers.CharField(source="get_type_display")  # noqa: A003

    class Meta:
        """Email Notification Model Serializer Metadata."""
        model = models.notifications.EmailNotification
        fields = ("id", "name", "type", "email", "catalogue_entry")


class WebhookNotificationSerializer(serializers.ModelSerializer):
    """Webhook Notification Model Serializer."""
    type = serializers.CharField(source="get_type_display")  # noqa: A003

    class Meta:
        """Webhook Notification Model Serializer Metadata."""
        model = models.notifications.WebhookNotification
        fields = ("id", "name", "type", "url", "catalogue_entry")
