"""
Test Cases for list rentals
"""
from datetime import date
from io import StringIO

from django.test import TestCase

from apps.bink.functions.lease_rent import lease_rent

from ..functions import list_rentals
from .factories import UnitFactory, reset


class TestListRentals(TestCase):
    "Test cases for fetch"

    def test_1_returns_list_rentals(self):
        "Is the output equal to what we put in?"
        lease_years = 2
        reset()
        UnitFactory(
            lease__years=lease_years,
            lease__rent=42,
            lease__started=date(2001, 1, 1),
            lease__stopped=date(2003, 3, 3),
            lease__review=date(2002, 2, 2),
        )
        expected = (
            "Units Reference,Unit Name,Tenant Name,Property Name,Property "
            "Address,Lease Start Date,Lease End Date,Lease Years,Next Rent "
            "Review,Current Rent,Unit type\r\n"
            "ref/0,Unit 0,Tenant Name #0,Property Name #0,XYZ 0AB,01-01-2001,"
            "03-03-2003,2,02-02-2002,42.00,unit 0\r\n\n"
        )
        output = StringIO()
        list_rentals.list_rentals(output=output)
        returned = output.getvalue()
        self.assertEqual(returned, expected)
