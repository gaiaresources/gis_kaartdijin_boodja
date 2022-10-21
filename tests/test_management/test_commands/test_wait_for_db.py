"""Provides unit tests for the Django Wait-for-DB Management Command."""


# Third-Party
from django import db
from django.core import management
import pytest
import pytest_mock


@pytest.mark.django_db()
def test_wait_for_db_up() -> None:
    """Tests management command when the database is up."""
    # Wait for Database
    management.call_command("wait_for_db", interval=0.0, attempts=1)


@pytest.mark.django_db()
def test_wait_for_db_down_then_up(mocker: pytest_mock.MockerFixture) -> None:
    """Tests management command when the database is down then up.

    Args:
        mocker (pytest_mock.MockerFixture): Pytest mocking fixture.
    """
    # Mock the Database Down and then Up
    mocker.patch(
        target="django.db.connection.ensure_connection",
        side_effect=[db.OperationalError, None],
    )

    # Wait for Database
    management.call_command("wait_for_db", interval=0.0, attempts=2)


@pytest.mark.django_db()
def test_wait_for_db_down(mocker: pytest_mock.MockerFixture) -> None:
    """Tests management command when the database is down.

    Args:
        mocker (pytest_mock.MockerFixture): Pytest mocking fixture.
    """
    # Mock the Database Down
    mocker.patch(
        target="django.db.connection.ensure_connection",
        side_effect=db.OperationalError,
    )

    # Assert Failure
    with pytest.raises(SystemExit):
        # Wait for Database
        management.call_command("wait_for_db", interval=0.0, attempts=1)
