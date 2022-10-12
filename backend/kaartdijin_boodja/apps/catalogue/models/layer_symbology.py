"""Kaartdijin Boodja Catalogue Django Application Layer Symbology Models."""


# Third-Party
from django.db import models

# Local
from . import catalogue_entries


class LayerSymbology(models.Model):
    """Model for a Layer Symbology."""
    name = models.TextField()
    file = models.URLField()
    catalogue_entry = models.ForeignKey(catalogue_entries.CatalogueEntry, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.name}"
