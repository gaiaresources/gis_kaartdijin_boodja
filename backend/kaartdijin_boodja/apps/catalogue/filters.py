"""Kaartdijin Boodja Catalogue Django Application Filters."""


# Third-Party
from django_filters import rest_framework as filters

# Local
from . import models


class CatalogueEntryFilter(filters.FilterSet):
    """Catalogue Entry Filter."""
    updated = filters.IsoDateTimeFromToRangeFilter(field_name="updated_at")

    class Meta:
        """Catalogue Entry Filter Metadata"""
        model = models.catalogue_entries.CatalogueEntry
        fields = ("assigned_to", "custodian", "status", "updated")


class EmailNotificationFilter(filters.FilterSet):
    """Email Notification Filter."""
    class Meta:
        """Email Notification Filter Metadata"""
        model = models.email_notifications.EmailNotification
        fields = ["name"]


class LayerAttributeFilter(filters.FilterSet):
    """Layer Attribute Filter."""
    class Meta:
        """Layer Attribute Filter Metadata"""
        model = models.layer_attributes.LayerAttribute
        fields = ["name"]


class LayerMetadataFilter(filters.FilterSet):
    """Layer Metadata Filter."""
    class Meta:
        """Layer Metadata Filter Metadata."""
        model = models.layer_metadata.LayerMetadata
        fields = ["name"]


class LayerSubmissionFilter(filters.FilterSet):
    """Layer Submission Filter."""
    class Meta:
        """Layer Submission Filter Metadata"""
        model = models.layer_submissions.LayerSubmission
        fields = ["name"]


class LayerSubscriptionFilter(filters.FilterSet):
    """Layer Subscription Filter."""
    class Meta:
        """Layer Subscription Filter Metadata"""
        model = models.layer_subscriptions.LayerSubscription
        fields = ["name"]


class LayerSymbologyFilter(filters.FilterSet):
    """Layer Symbology Filter."""
    class Meta:
        """Layer Symbology Filter Metadata"""
        model = models.layer_symbology.LayerSymbology
        fields = ["name"]


class WebhookNotificationFilter(filters.FilterSet):
    """Webhook Notification Filter."""
    class Meta:
        """Webhook Notification Filter Metadata"""
        model = models.webhook_notifications.WebhookNotification
        fields = ["name"]
