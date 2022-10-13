"""Kaartdijin Boodja Catalogue Django Serializers."""


# Third-Party
from rest_framework import serializers

# Local
from .. import models


class EmailNotificationSerializer(serializers.ModelSerializer):
    """Email Notification Model Serializer."""
    type = serializers.CharField(source="get_type_display")

    class Meta:
        """Email Notification Model Serializer Metadata."""
        model = models.email_notifications.EmailNotification
        fields = ("id", "name", "type", "email", "catalogue_entry")
