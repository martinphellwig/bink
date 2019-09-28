"""
This module contains the store function which is used in the django command
tenant_masts function.
"""
import sys
from pprint import pprint

from django import db

from .. import models

DEFAULT = 25


def tenant_masts(years=DEFAULT, output=sys.stdout):
    "Return a pretty print of a dict tenants as key and count mast as value."
    qs = (
        models.Unit.objects.all()
        .order_by("tenant__name")
        .values("tenant__name")
        .annotate(db.models.Count("reference"))
    )
    returns = {row["tenant__name"]: row["reference__count"] for row in qs}
    pprint(returns, stream=output)
