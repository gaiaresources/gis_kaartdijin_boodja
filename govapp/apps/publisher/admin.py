"""Kaartdijin Boodja Publisher Django Application Administration."""


# Third-Party
from django.contrib import admin
import reversion.admin

# Local
from govapp.apps.publisher import models


class PublishEntryAdmin(reversion.admin.VersionAdmin):
    """Custom Django Admin for Publish Entries."""
    # This provides a better interface for `ManyToMany` fields
    # See: https://stackoverflow.com/questions/5385933/a-better-django-admin-manytomany-field-widget
    filter_horizontal = ["editors"]


# Register Models
admin.site.register(models.publish_channels.CDDPPublishChannel, reversion.admin.VersionAdmin)
admin.site.register(models.publish_channels.GeoServerPublishChannel, reversion.admin.VersionAdmin)
admin.site.register(models.publish_entries.PublishEntry, PublishEntryAdmin)
admin.site.register(models.notifications.EmailNotification, reversion.admin.VersionAdmin)
admin.site.register(models.workspaces.Workspace, reversion.admin.VersionAdmin)
