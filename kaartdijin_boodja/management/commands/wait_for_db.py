"""Kaartdijin Boodja Django Project Wait-for-Database Management Command."""


# Standard
import argparse
import sys
import time

# Third-Party
from django import db
from django.core.management import base

# Typing
from typing import Any


# Constants
DEFAULT_INTERVAL_S = 3.0
DEFAULT_ATTEMPTS = 60


class Command(base.BaseCommand):
    """Wait-for-Database Management Command."""
    # Help string
    help = "Blocks until the database is available"  # noqa: A003

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Adds command-line arguments to the management command.

        Args:
            parser (argparse.ArgumentParser): Argument parser to add to.
        """
        # Add arguments
        parser.add_argument("--interval", type=float, default=DEFAULT_INTERVAL_S)
        parser.add_argument("--attempts", type=int, default=DEFAULT_ATTEMPTS)

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Handles the management command functionality."""
        # Retrieve command-line arguments
        interval = kwargs["interval"]
        attempts = kwargs["attempts"]

        # Loop
        for retry in range(attempts):
            # Handle database connection errors
            try:
                # Test connection
                db.connection.ensure_connection()

            except db.OperationalError as exc:
                # Display attempt error
                self.stdout.write(
                    f"Database unavailable on attempt {retry + 1}/{attempts}: {exc}"
                )

                # Sleep
                time.sleep(interval)

            else:
                # Success!
                self.stdout.write(self.style.SUCCESS("Database available"))
                break
        else:
            # Failure
            self.stdout.write(self.style.ERROR("Database unavailable"))
            sys.exit(1)
