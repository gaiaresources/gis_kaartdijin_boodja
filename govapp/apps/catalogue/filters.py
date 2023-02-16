"""Kaartdijin Boodja Catalogue Django Application Filters."""


# Third-Party
from django_filters import rest_framework as filters

# Local
from govapp.apps.catalogue import models


class CatalogueEntryFilter(filters.FilterSet):
    """Catalogue Entry Filter."""
    updated = filters.IsoDateTimeFromToRangeFilter(field_name="updated_at")
    order_by = filters.OrderingFilter(fields=("id", "name", "status", "updated_at", "custodian", "assigned_to"))

    class Meta:
        """Catalogue Entry Filter Metadata."""
        model = models.catalogue_entries.CatalogueEntry
        fields = {"id": ["in"], "assigned_to": ["exact"], "custodian": ["exact"], "status": ["in", "exact"]}


class CustodianFilter(filters.FilterSet):
    """Custodian Filter."""
    class Meta:
        """Custodian Filter Metadata."""
        model = models.custodians.Custodian
        fields = ()


class LayerAttributeFilter(filters.FilterSet):
    """Layer Attribute Filter."""
    class Meta:
        """Layer Attribute Filter Metadata."""
        model = models.layer_attributes.LayerAttribute
        fields = {"catalogue_entry": ["in"]}


class LayerMetadataFilter(filters.FilterSet):
    """Layer Metadata Filter."""
    class Meta:
        """Layer Metadata Filter Metadata.."""
        model = models.layer_metadata.LayerMetadata
        fields = ()


class LayerSubmissionFilter(filters.FilterSet):
    """Layer Submission Filter."""
    submitted = filters.IsoDateTimeFromToRangeFilter(field_name="submitted_at")
    order_by = filters.OrderingFilter(
        fields=(
            "id",
            ("catalogue_entry__name", "name"),  # Proxy through the Catalogue Entry name to sort by
            "status",
            "submitted_at",
        ),
    )

    class Meta:
        """Layer Submission Filter Metadata."""
        model = models.layer_submissions.LayerSubmission
        fields = ("status", "submitted", "is_active")


class LayerSubscriptionFilter(filters.FilterSet):
    """Layer Subscription Filter."""
    subscribed = filters.IsoDateTimeFromToRangeFilter(field_name="subscribed_at")
    order_by = filters.OrderingFilter(
        fields=(
            "id",
            ("catalogue_entry__name", "name"),  # Proxy through the Catalogue Entry name to sort by
            "url",
            "status",
            "subscribed_at",
        )
    )

    class Meta:
        """Layer Subscription Filter Metadata."""
        model = models.layer_subscriptions.LayerSubscription
        fields = ("status", "subscribed")


class LayerSymbologyFilter(filters.FilterSet):
    """Layer Symbology Filter."""
    class Meta:
        """Layer Symbology Filter Metadata."""
        model = models.layer_symbology.LayerSymbology
        fields = {"catalogue_entry"}


class EmailNotificationFilter(filters.FilterSet):
    """Email Notification Filter."""
    class Meta:
        """Email Notification Filter Metadata."""
        model = models.notifications.EmailNotification
        fields = {"id": ["in"]}


class WebhookNotificationFilter(filters.FilterSet):
    """Webhook Notification Filter."""
    class Meta:
        """Webhook Notification Filter Metadata."""
        model = models.notifications.WebhookNotification
        fields = {"id": ["in"]}
