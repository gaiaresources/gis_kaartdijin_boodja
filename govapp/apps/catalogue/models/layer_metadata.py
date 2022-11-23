"""Kaartdijin Boodja Catalogue Django Application Layer Metadata Models."""


# Third-Party
from django.db import models

# Local
from . import catalogue_entries


class LayerMetadata(models.Model):
    """Model for a Layer Metadata."""
    name = models.TextField()
    created_at = models.DateTimeField()
    catalogue_entry = models.OneToOneField(
        catalogue_entries.CatalogueEntry,
        related_name="metadata",
        on_delete=models.CASCADE,
    )

    class Meta:
        """Layer Metadata Model Metadata."""
        verbose_name = "Layer Metadata"
        verbose_name_plural = "Layer Metadata"

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.name}"
