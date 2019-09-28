"""
This command stores the specified filename in the database.
"""

import argparse
import os

from django.core.management.base import BaseCommand

from ...functions import store


def _check_path(value):
    path = os.path.abspath(value)
    if not os.path.exists(path):
        text = "Path '{}' does not exist ({})."
        raise argparse.ArgumentTypeError(text.format(value, path))

    return path


class Command(BaseCommand):
    "Django Command; `store`."
    help = """
    Store the specified file in the database.
    """

    def add_arguments(self, parser):
        help_text = """
        Specify the location of the CSV file and add its contents to the DB.
        """

        parser.add_argument("csv_file", type=_check_path, help=help_text)

    def handle(self, *args, **options):
        store.store(options["csv_file"])
