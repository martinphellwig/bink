"""
This module contains the store function which is used in the django command
store function.
"""
import sys
from csv import writer
from io import StringIO

from django import db

from .. import models
from .store import MAP_FIELDS

DEFAULT = 25


def _make_row(instance):
    row = []

    for model, attribute in MAP_FIELDS.values():
        if model == "Unit":
            fetch_instance = instance
        else:
            name = model.lower()
            if name == "unittype":
                name = "unit_type"
            fetch_instance = getattr(instance, name)

        value = getattr(fetch_instance, attribute)
        row.append(value)

    return row


def lease_rent(years=DEFAULT, output=sys.stdout):
    ""
    file_like_object = StringIO()
    csv = writer(file_like_object)

    masts = models.Unit.objects.filter(lease__years=years)
    csv.writerow(MAP_FIELDS.keys())

    for instance in masts:
        row = _make_row(instance)
        csv.writerow(row)

    print(file_like_object.getvalue(), file=output)

    total_rent = masts.aggregate(sum=db.models.Sum("lease__rent"))
    print("Total Rent: {}".format(total_rent["sum"]), file=output)
