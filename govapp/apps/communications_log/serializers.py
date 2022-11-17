"""Kaartdijin Boodja Communications Log Django Serializers."""


# Third-Party
from rest_framework import serializers

# Local
from . import models


class LogEntrySerializer(serializers.ModelSerializer):
    """Log Entry Model Serializer."""
    class Meta:
        """Log Entry Model Serializer Metadata."""
        model = models.LogEntry
        fields = (
            "id",
            "to",
            "fromm",
            "cc",
            "type",
            "reference",
            "subject",
            "text",
            "customer",
            "staff",
            "created",
            "attachments",
        )
