"""Kaartdijin Boodja Catalogue Django Application Emails."""


# Third-Party
from ..emails import emails


class CatalogueEntryLockedEmail(emails.TemplateEmailBase):
    """Catalogue Entry Locked Email Abstraction."""
    subject = "A Catalogue Entry has been updated"
    html_template = "catalogue_entry_locked_email.html"
    txt_template = "catalogue_entry_locked_email.txt"
