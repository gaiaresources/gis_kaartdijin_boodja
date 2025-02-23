"""Kaartdijin Boodja Publisher Django Application Views."""


# Third-Party
from django import shortcuts
from django.contrib import auth
from drf_spectacular import utils as drf_utils
from rest_framework import decorators
from rest_framework import request
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

# Local
from govapp.common import mixins
from govapp.common import utils
from govapp.apps.logs import mixins as logs_mixins
from govapp.apps.logs import utils as logs_utils
from govapp.apps.publisher import filters
from govapp.apps.publisher import models
from govapp.apps.publisher import permissions
from govapp.apps.publisher import serializers

# Typing
from typing import cast


# Shortcuts
UserModel = auth.get_user_model()


@drf_utils.extend_schema(tags=["Publisher - Publish Entries"])
class PublishEntryViewSet(
    mixins.ChoicesMixin,
    mixins.MultipleSerializersMixin,
    logs_mixins.ActionsLogMixin,
    logs_mixins.CommunicationsLogMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Publish Entry View Set."""
    queryset = models.publish_entries.PublishEntry.objects.all()
    serializer_class = serializers.publish_entries.PublishEntrySerializer
    serializer_classes = {"create": serializers.publish_entries.PublishEntryCreateSerializer}
    filterset_class = filters.PublishEntryFilter
    search_fields = ["description", "catalogue_entry__name"]
    permission_classes = [permissions.IsPublishEntryPermissions]

    @drf_utils.extend_schema(
        parameters=[drf_utils.OpenApiParameter("symbology_only", type=bool)],
        request=None,
        responses={status.HTTP_204_NO_CONTENT: None},
    )
    @decorators.action(detail=True, methods=["POST"])
    def publish(self, request: request.Request, pk: str) -> response.Response:
        """Publishes to both channels.

        Args:
            request (request.Request): API request.
            pk (str): Primary key of the Publish Entry.

        Returns:
            response.Response: Empty response confirming success.
        """
        # Retrieve Publish Entry
        # Help `mypy` by casting the resulting object to a Publish Entry
        publish_entry = self.get_object()
        publish_entry = cast(models.publish_entries.PublishEntry, publish_entry)

        # Retrieve `symbology_only` Query Parameter
        symbology_only = self.request.query_params.get("symbology_only")
        symbology_only = utils.string_to_boolean(symbology_only)  # type: ignore[assignment]

        # Publish!
        publish_entry.publish(symbology_only)

        # Add Action Log Entry
        logs_utils.add_to_actions_log(
            user=request.user,
            model=publish_entry,
            action="Publish entry was manually re-published to both channels"
        )

        # Return Response
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @drf_utils.extend_schema(
        parameters=[drf_utils.OpenApiParameter("symbology_only", type=bool)],
        request=None,
        responses={status.HTTP_204_NO_CONTENT: None},
    )
    @decorators.action(detail=True, methods=["POST"], url_path=r"publish/cddp")
    def publish_cddp(self, request: request.Request, pk: str) -> response.Response:
        """Publishes to the CDDP Channel.

        Args:
            request (request.Request): API request.
            pk (str): Primary key of the Publish Entry.

        Returns:
            response.Response: Empty response confirming success.
        """
        # Retrieve Publish Entry
        # Help `mypy` by casting the resulting object to a Publish Entry
        publish_entry = self.get_object()
        publish_entry = cast(models.publish_entries.PublishEntry, publish_entry)

        # Retrieve `symbology_only` Query Parameter
        symbology_only = self.request.query_params.get("symbology_only")
        symbology_only = utils.string_to_boolean(symbology_only)  # type: ignore[assignment]

        # Publish!
        publish_entry.publish_cddp(symbology_only)

        # Add Action Log Entry
        logs_utils.add_to_actions_log(
            user=request.user,
            model=publish_entry,
            action="Publish entry was manually re-published to the CDDP channel"
        )

        # Return Response
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @drf_utils.extend_schema(
        parameters=[drf_utils.OpenApiParameter("symbology_only", type=bool)],
        request=None,
        responses={status.HTTP_204_NO_CONTENT: None},
    )
    @decorators.action(detail=True, methods=["POST"], url_path=r"publish/geoserver")
    def publish_geoserver(self, request: request.Request, pk: str) -> response.Response:
        """Publishes to the GeoServer Channel.

        Args:
            request (request.Request): API request.
            pk (str): Primary key of the Publish Entry.

        Returns:
            response.Response: Empty response confirming success.
        """
        # Retrieve Publish Entry
        # Help `mypy` by casting the resulting object to a Publish Entry
        publish_entry = self.get_object()
        publish_entry = cast(models.publish_entries.PublishEntry, publish_entry)

        # Retrieve `symbology_only` Query Parameter
        symbology_only = self.request.query_params.get("symbology_only")
        symbology_only = utils.string_to_boolean(symbology_only)  # type: ignore[assignment]

        # Publish!
        publish_entry.publish_geoserver(symbology_only)

        # Add Action Log Entry
        logs_utils.add_to_actions_log(
            user=request.user,
            model=publish_entry,
            action="Publish entry was manually re-published to the GeoServer channel"
        )

        # Return Response
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @drf_utils.extend_schema(request=None, responses={status.HTTP_204_NO_CONTENT: None})
    @decorators.action(detail=True, methods=["POST"])
    def lock(self, request: request.Request, pk: str) -> response.Response:
        """Locks the Publish Entry.

        Args:
            request (request.Request): API request.
            pk (str): Primary key of the Publish Entry.

        Returns:
            response.Response: Empty response confirming success.
        """
        # Retrieve Publish Entry
        # Help `mypy` by casting the resulting object to a Publish Entry
        publish_entry = self.get_object()
        publish_entry = cast(models.publish_entries.PublishEntry, publish_entry)

        # Lock
        success = publish_entry.lock()

        # Check Success
        if success:
            # Add Action Log Entry
            logs_utils.add_to_actions_log(
                user=request.user,
                model=publish_entry,
                action="Publish entry was locked"
            )

        # Return Response
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @drf_utils.extend_schema(request=None, responses={status.HTTP_204_NO_CONTENT: None})
    @decorators.action(detail=True, methods=["POST"])
    def unlock(self, request: request.Request, pk: str) -> response.Response:
        """Unlocks the Publish Entry.

        Args:
            request (request.Request): API request.
            pk (str): Primary key of the Publish Entry.

        Returns:
            response.Response: Empty response confirming success.
        """
        # Retrieve Publish Entry
        # Help `mypy` by casting the resulting object to a Publish Entry
        publish_entry = self.get_object()
        publish_entry = cast(models.publish_entries.PublishEntry, publish_entry)

        # Unlock
        success = publish_entry.unlock()

        # Check Success
        if success:
            # Add Action Log Entry
            logs_utils.add_to_actions_log(
                user=request.user,
                model=publish_entry,
                action="Publish entry was unlocked"
            )

        # Return Response
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @drf_utils.extend_schema(request=None, responses={status.HTTP_204_NO_CONTENT: None})
    @decorators.action(detail=True, methods=["POST"], url_path=r"assign/(?P<user_pk>\d+)")
    def assign(self, request: request.Request, pk: str, user_pk: str) -> response.Response:
        """Assigns the Publish Entry.

        Args:
            request (request.Request): API request.
            pk (str): Primary key of the Publish Entry.
            user_pk (str): Primary key of the User to assign to.

        Returns:
            response.Response: Empty response confirming success.
        """
        # Retrieve Publish Entry
        # Help `mypy` by casting the resulting object to a Publish Entry
        publish_entry = self.get_object()
        publish_entry = cast(models.publish_entries.PublishEntry, publish_entry)

        # Retrieve User
        user = shortcuts.get_object_or_404(UserModel, id=user_pk)

        # Assign!
        success = publish_entry.assign(user)

        # Check Success
        if success:
            # Add Action Log Entry
            logs_utils.add_to_actions_log(
                user=request.user,
                model=publish_entry,
                action=f"Publish entry was assigned to {user} (id: {user.pk})"
            )

        # Return Response
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    @drf_utils.extend_schema(request=None, responses={status.HTTP_204_NO_CONTENT: None})
    @decorators.action(detail=True, methods=["POST"])
    def unassign(self, request: request.Request, pk: str) -> response.Response:
        """Unassigns the Publish Entry.

        Args:
            request (request.Request): API request.
            pk (str): Primary key of the Publish Entry.

        Returns:
            response.Response: Empty response confirming success.
        """
        # Retrieve Publish Entry
        # Help `mypy` by casting the resulting object to a Publish Entry
        publish_entry = self.get_object()
        publish_entry = cast(models.publish_entries.PublishEntry, publish_entry)

        # Unassign!
        success = publish_entry.unassign()

        # Check Success
        if success:
            # Add Action Log Entry
            logs_utils.add_to_actions_log(
                user=request.user,
                model=publish_entry,
                action="Publish entry was unassigned"
            )

        # Return Response
        return response.Response(status=status.HTTP_204_NO_CONTENT)


@drf_utils.extend_schema(tags=["Publisher - CDDP Publish Channels"])
class CDDPPublishChannelViewSet(
    mixins.ChoicesMixin,
    mixins.MultipleSerializersMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """CDDP Publish Channel View Set."""
    queryset = models.publish_channels.CDDPPublishChannel.objects.all()
    serializer_class = serializers.publish_channels.CDDPPublishChannelSerializer
    serializer_classes = {"create": serializers.publish_channels.CDDPPublishChannelCreateSerializer}
    filterset_class = filters.CDDPPublishChannelFilter
    search_fields = ["publish_entry__catalogue_entry__name", "publish_entry__description"]
    permission_classes = [permissions.HasPublishEntryPermissions]


@drf_utils.extend_schema(tags=["Publisher - GeoServer Publish Channels"])
class GeoServerPublishChannelViewSet(
    mixins.ChoicesMixin,
    mixins.MultipleSerializersMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """GeoServer Publish Channel View Set."""
    queryset = models.publish_channels.GeoServerPublishChannel.objects.all()
    serializer_class = serializers.publish_channels.GeoServerPublishChannelSerializer
    serializer_classes = {"create": serializers.publish_channels.GeoServerPublishChannelCreateSerializer}
    filterset_class = filters.GeoServerPublishChannelFilter
    search_fields = ["publish_entry__catalogue_entry__name", "publish_entry__description"]
    permission_classes = [permissions.HasPublishEntryPermissions]


@drf_utils.extend_schema(tags=["Publisher - Notifications (Email)"])
class EmailNotificationViewSet(
    mixins.ChoicesMixin,
    mixins.MultipleSerializersMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Email Notification View Set."""
    queryset = models.notifications.EmailNotification.objects.all()
    serializer_class = serializers.notifications.EmailNotificationSerializer
    serializer_classes = {"create": serializers.notifications.EmailNotificationCreateSerializer}
    filterset_class = filters.EmailNotificationFilter
    search_fields = ["name", "email"]
    permission_classes = [permissions.HasPublishEntryPermissions]


@drf_utils.extend_schema(tags=["Publisher - Workspaces"])
class WorkspaceViewSet(mixins.ChoicesMixin, viewsets.ReadOnlyModelViewSet):
    """Workspace View Set."""
    queryset = models.workspaces.Workspace.objects.all()
    serializer_class = serializers.workspaces.WorkspaceSerializer
    filterset_class = filters.WorkspaceFilter
    search_fields = ["name"]
