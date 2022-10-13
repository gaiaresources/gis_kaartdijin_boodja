"""Kaartdijin Boodja Catalogue Django Application Views."""


# Third-Party
from rest_framework import viewsets

# Local
from . import serializers
from . import models


class CatalogueEntryViewSet(viewsets.ReadOnlyModelViewSet):
    """Catalogue Entry View Set."""
    queryset = models.catalogue_entries.CatalogueEntry.objects.all()
    serializer_class = serializers.catalogue_entries.CatalogueEntrySerializer


class EmailNotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """Email Notification View Set."""
    queryset = models.email_notifications.EmailNotification.objects.all()
    serializer_class = serializers.email_notifications.EmailNotificationSerializer


class LayerAttributeViewSet(viewsets.ReadOnlyModelViewSet):
    """Layer Attribute View Set."""
    queryset = models.layer_attributes.LayerAttribute.objects.all()
    serializer_class = serializers.layer_attributes.LayerAttributeSerializer


class LayerMetadataViewSet(viewsets.ReadOnlyModelViewSet):
    """Layer Metadata View Set."""
    queryset = models.layer_metadata.LayerMetadata.objects.all()
    serializer_class = serializers.layer_metadata.LayerMetadataSerializer


class LayerSubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    """Layer Submission View Set."""
    queryset = models.layer_submissions.LayerSubmission.objects.all()
    serializer_class = serializers.layer_submissions.LayerSubmissionSerializer


class LayerSubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    """Layer Subscription View Set."""
    queryset = models.layer_subscriptions.LayerSubscription.objects.all()
    serializer_class = serializers.layer_subscriptions.LayerSubscriptionSerializer


class LayerSymbologyViewSet(viewsets.ReadOnlyModelViewSet):
    """Layer Symbology View Set."""
    queryset = models.layer_symbology.LayerSymbology.objects.all()
    serializer_class = serializers.layer_symbology.LayerSymbologySerializer


class WebhookNotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """Webhook Notification View Set."""
    queryset = models.webhook_notifications.WebhookNotification.objects.all()
    serializer_class = serializers.webhook_notifications.WebhookNotificationSerializer
