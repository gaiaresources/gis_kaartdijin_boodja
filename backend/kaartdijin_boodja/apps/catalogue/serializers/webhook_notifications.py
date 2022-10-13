"""Kaartdijin Boodja Catalogue Django Serializers."""


# Third-Party
from rest_framework import serializers

# Local
from .. import models


class WebhookNotificationSerializer(serializers.ModelSerializer):
    """Webhook Notification Model Serializer."""
    type = serializers.CharField(source="get_type_display")

    class Meta:
        """Webhook Notification Model Serializer Metadata."""
        model = models.webhook_notifications.WebhookNotification
        fields = ("id", "name", "type", "url")
