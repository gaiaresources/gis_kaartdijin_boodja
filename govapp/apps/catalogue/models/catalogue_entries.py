"""Kaartdijin Boodja Catalogue Django Application Catalogue Entry Models."""


# Third-Party
from django.contrib import auth
from django.db import models

# Local
from .. import emails

# Typing
from typing import Optional, Iterable


# Shortcuts
UserModel = auth.get_user_model()  # TODO -> Does this work with SSO?


class CatalogueEntryStatus(models.IntegerChoices):
    """Enumeration for a Catalogue Entry Status."""
    DRAFT = 1
    LOCKED = 2
    CANCELLED = 3


class CatalogueEntry(models.Model):
    """Model for a Catalogue Entry."""
    name = models.TextField()
    description = models.TextField()
    active_layer = models.OneToOneField(
        "catalogue.LayerSubmission",
        default=None,
        blank=True,
        null=True,
        related_name="+",  # No backwards relation
        on_delete=models.PROTECT,
    )
    status = models.IntegerField(choices=CatalogueEntryStatus.choices, default=CatalogueEntryStatus.DRAFT)
    updated_at = models.DateTimeField(auto_now=True)
    custodian = models.ForeignKey(
        UserModel,
        default=None,
        blank=True,
        null=True,
        related_name="custody",
        on_delete=models.SET_NULL,
    )
    assigned_to = models.ForeignKey(
        UserModel,
        default=None,
        blank=True,
        null=True,
        related_name="assigned",
        on_delete=models.SET_NULL,
    )

    class Meta:
        """Catalogue Entry Model Metadata."""
        verbose_name = "Catalogue Entry"
        verbose_name_plural = "Catalogue Entries"

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.name}"

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: Optional[str] = None,
        update_fields: Optional[Iterable[str]] = None,
    ) -> None:
        """Overrides the model save function to provide on-save hooks.

        Args:
            force_insert (bool): Whether to force insert.
            force_update (bool): Whether to force update.
            using (Optional[str]): Database to use.
            update_fields (Optional[Iterable[str]]): Fields to be updated.
        """
        # Get current status from database
        # If this is the first time the model is being created, then this will
        # not exist in the database yet and `None` will be returned
        current = CatalogueEntry.objects.filter(id=self.id).first()

        # Save
        super().save(force_insert, force_update, using, update_fields)

        # Check for Status Change to Locked
        if (
            current  # The catalogue entry already existed in the database
            and current.status != self.status  # The status changed
            and self.status == CatalogueEntryStatus.LOCKED  # The new status is LOCKED
        ):
            # Email Notifications!
            for en in self.email_notifications.all():
                # Send Email Notification
                emails.CatalogueEntryLockedEmail().send(en.email)

            # Webhook Notifications!
            for wn in self.webhook_notifications.all():
                # Send Webhook Notification
                wn  # TODO -> Send webhook notifications
