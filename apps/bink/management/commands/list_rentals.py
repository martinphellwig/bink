"""
This command implements requirements 4
"""
import argparse
from datetime import datetime

from django.core.management.base import BaseCommand

from ...functions import list_rentals


def _check_date(value):
    try:
        parsed = datetime.strptime(value, list_rentals.DATE_FORMAT)
    except ValueError:
        text = """
        Date '{}' in incorrect format, it should be: dd-mm-yyyy.
        """
        raise argparse.ArgumentTypeError(text.format(value))
    value = parsed.strftime(list_rentals.DATE_FORMAT)
    return value


class Command(BaseCommand):
    "Django Command; `list_rentals`."
    help = """
    Returns a list of rentals.
    """

    def add_arguments(self, parser):
        help_text_from = """
        Specify the from date, by default this is: '%(default)s'.
        """

        parser.add_argument(
            "--from",
            type=_check_date,
            default=list_rentals.DEFAULT_DATE_FROM,
            help=help_text_from,
        )

        help_text_till = """
        Specify the till date, by default this is: '%(default)s'.
        """

        parser.add_argument(
            "--till",
            type=_check_date,
            default=list_rentals.DEFAULT_DATE_TILL,
            help=help_text_till,
        )

    def handle(self, *args, **options):
        list_rentals.list_rentals(options["from"], options["till"])
