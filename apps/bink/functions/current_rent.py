"""
This module contains the current rent function which is used in the django
command current_rent function.
"""
import sys

from .. import models
from .common import make_csv_from_unit_queryset

DEFAULT = 5


def current_rent(max_items=DEFAULT, output=sys.stdout):
    "lease rent command functionality."
    queryset = models.Unit.objects.all().order_by("lease__rent")[:max_items]
    csv_out = make_csv_from_unit_queryset(queryset)
    print(csv_out, file=output)
