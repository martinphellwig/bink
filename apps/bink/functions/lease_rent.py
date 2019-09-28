"""
This module contains the store function which is used in the django command
store function.
"""
import sys

from django import db

from .. import models
from .common import make_csv_from_unit_queryset

DEFAULT = 25


def lease_rent(years=DEFAULT, output=sys.stdout):
    "lease rent command functionality."
    queryset = models.Unit.objects.filter(lease__years=years)
    csv_out = make_csv_from_unit_queryset(queryset)
    print(csv_out, file=output)

    total_rent = queryset.aggregate(sum=db.models.Sum("lease__rent"))
    print("Total Rent: {}".format(total_rent["sum"]), file=output)
