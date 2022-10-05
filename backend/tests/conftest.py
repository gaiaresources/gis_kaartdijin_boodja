"""Provides configuration, fixtures, and plugins for pytest.

It may be also used for extending doctest's context:
    1. https://docs.python.org/3/library/doctest.html
    2. https://docs.pytest.org/en/latest/doctest.html
"""


# Third-Party
import pytest
from pytest_django import fixtures


@pytest.fixture(autouse=True)
def _debug(settings: fixtures.SettingsWrapper) -> None:
    """Sets proper DEBUG and TEMPLATE debug mode for coverage.

    Args:
        settings (fixtures.SettingsWrapper): Pytest Django settings fixture.
    """
    # Set debug flag to false
    settings.DEBUG = False

    # Set templates to debug mode
    for template in settings.TEMPLATES:
        template["OPTIONS"]["debug"] = True
