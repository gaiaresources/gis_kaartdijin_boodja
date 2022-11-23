"""Kaartdijin Boodja Catalogue Django Application Administration."""


# Third-Party
from rest_framework import permissions
from rest_framework import request
from rest_framework import views


class CatalogueEditorAndAssignedPermission(permissions.BasePermission):
    """_summary_."""

    def has_permission(self, request: request.Request, view: views.APIView) -> bool:
        """_summary_.

        Args:
            request (request.Request): _description_
            view (views.APIView): _description_

        Returns:
            bool: _description_
        """
        # Check if method is safe
        if request.method in permissions.SAFE_METHODS:
            # Done!
            return True

        # TODO
        return False
