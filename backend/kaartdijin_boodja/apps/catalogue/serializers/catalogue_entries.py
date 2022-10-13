"""Kaartdijin Boodja Catalogue Django Serializers."""


# Third-Party
from rest_framework import serializers

# Local
from .. import models


class CatalogueEntrySerializer(serializers.ModelSerializer):
    """Catalogue Entry Model Serializer."""
    status = serializers.CharField(source="get_status_display")
    custodian = serializers.StringRelatedField()  # type: ignore[var-annotated]
    assigned_to = serializers.StringRelatedField()  # type: ignore[var-annotated]

    class Meta:
        """Catalogue Entry Model Serializer Metadata."""
        model = models.catalogue_entries.CatalogueEntry
        fields = ("id", "name", "description", "status", "updated_at", "custodian", "assigned_to")
