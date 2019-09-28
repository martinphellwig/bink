"""
This command implements requirements 1
"""
from django.core.management.base import BaseCommand

from ...functions import current_rent


class Command(BaseCommand):
    "Django Command; `lease_rent`."
    help = """
    Returns a list of current rent sorted in ascending order of rent.
    """

    def add_arguments(self, parser):
        help_text = """
        Specify the max amount of items, by default this
        is: '%(default)s'."""

        parser.add_argument(
            "--max", type=int, default=current_rent.DEFAULT, help=help_text
        )

    def handle(self, *args, **options):
        current_rent.current_rent(options["max"])
