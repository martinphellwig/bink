"""
This module contains the list_rental function which is used in the django
command list_rental function.
"""
import sys
from datetime import datetime

from .. import models
from .common import DATE_FORMAT, make_csv_from_unit_queryset

DEFAULT_DATE_FROM = "01-06-1999"
DEFAULT_DATE_TILL = "31-08-2007"


def list_rentals(
    date_from=DEFAULT_DATE_FROM, date_till=DEFAULT_DATE_TILL, output=sys.stdout
):
    "list_rentals command functionality."
    _from = datetime.strptime(date_from, DATE_FORMAT).date()
    _till = datetime.strptime(date_till, DATE_FORMAT).date()
    queryset = models.Unit.objects.filter(
        lease__started__gte=_from, lease__started__lte=_till
    )
    csv_out = make_csv_from_unit_queryset(queryset)
    print(csv_out, file=output)
