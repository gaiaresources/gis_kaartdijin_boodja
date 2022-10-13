"""Kaartdijin Boodja Catalogue Django Serializers."""


# Third-Party
from rest_framework import serializers

# Local
from .. import models


class LayerAttributeSerializer(serializers.ModelSerializer):
    """Layer Attribute Model Serializer."""
    type = serializers.CharField(source="get_type_display")

    class Meta:
        """Layer Attribute Model Serializer Metadata."""
        model = models.layer_attributes.LayerAttribute
        fields = ("id", "name", "type", "order", "layer")
