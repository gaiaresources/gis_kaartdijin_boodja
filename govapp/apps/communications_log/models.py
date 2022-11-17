"""Kaartdijin Boodja Communications Log Django Application Models."""


# Third-Party
from django.contrib import auth
from django.db import models


# Shortcuts
UserModel = auth.get_user_model()  # TODO -> Does this work with SSO?


class LogEntryType(models.IntegerChoices):
    """Enumeration for a Log Entry Type."""
    EMAIL = 1
    PHONE_CALL = 2
    MAIL = 3
    PERSON = 4
    ON_HOLD = 5
    ON_HOLD_REMOVE = 6
    WITH_QA_OFFICER = 7
    WITH_QA_OFFICER_COMPLETED = 8
    REFERRAL_COMPLETED = 9


class LogEntry(models.Model):
    """Model for a Log Entry."""
    to = models.TextField(blank=True)
    fromm = models.TextField(blank=True)
    cc = models.TextField(blank=True)
    type = models.IntegerField(choices=LogEntryType.choices, default=LogEntryType.EMAIL)  # noqa: A003
    reference = models.TextField(blank=True)
    subject = models.TextField(blank=True)
    text = models.TextField(blank=True)
    customer = models.ForeignKey(UserModel, null=True, related_name="+", on_delete=models.SET_NULL)
    staff = models.ForeignKey(UserModel, null=True, related_name="+", on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        """Communications Log Entry Model Metadata."""
        verbose_name = "Communications Log Entry"
        verbose_name_plural = "Communications Log Entries"
        abstract = True

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.subject}"


class LogEntryAttachment(models.Model):
    """Model for a Log Entry Attachment."""
    name = models.TextField()
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

    class Meta:
        """Log Entry Attachment Model Metadata."""
        verbose_name = "Log Entry Attachment"
        verbose_name_plural = "Log Entry Attachments"
        abstract = True

    def __str__(self) -> str:
        """Provides a string representation of the object.

        Returns:
            str: Human readable string representation of the object.
        """
        # Generate String and Return
        return f"{self.name}"
