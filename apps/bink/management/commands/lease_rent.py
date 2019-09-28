"""
This command implements requirements 2
"""
from django.core.management.base import BaseCommand

from ...functions import lease_rent


class Command(BaseCommand):
    "Django Command; `lease_rent`."
    help = """
    Returns a list of filtered mast data and the total rent.
    """

    def add_arguments(self, parser):
        help_text = """
        Specify the lease year to filter on, by default this
        is: '%(default)s'."""

        parser.add_argument(
            "--years", type=int, default=lease_rent.DEFAULT, help=help_text
        )

    def handle(self, *args, **options):
        lease_rent.lease_rent(options["years"])
