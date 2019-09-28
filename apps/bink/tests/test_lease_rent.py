"""
Test Cases for Lease Rent
"""
from io import StringIO

from django.test import TestCase

from .. import models
from ..functions import lease_rent
from .factories import UnitFactory


class TestLeaseRent(TestCase):
    "Test cases for fetch"

    def test_1_returns_lease_rent(self):
        "Is the output equal to what we put in?"
        lease_years = 2
        UnitFactory(
            lease__years=lease_years,
            lease__rent=42,
            lease__started=None,
            lease__stopped=None,
            lease__review=None,
        )
        expected = (
            "Units Reference,Unit Name,Tenant Name,Property Name,Property "
            "Address,Lease Start Date,Lease End Date,Lease Years,Next Rent "
            "Review,Current Rent,Unit type\r\n"
            "ref/0,Unit 0,Tenant Name #0,Property Name #0,XYZ 0AB,,,2,,42.00,"
            "unit 0"
            "\r\n\nTotal Rent: 42\n"
        )
        output = StringIO()

        lease_rent.lease_rent(lease_years, output)
        self.assertEqual(output.getvalue(), expected)

    def test_2_returns_none_total(self):
        "If the selection is empty it should return None in total."
        UnitFactory(
            lease__years=25,
            lease__rent=42,
            lease__started=None,
            lease__stopped=None,
            lease__review=None,
        )
        output = StringIO()

        lease_rent.lease_rent(years=5, output=output)
        rent = output.getvalue().split("Total Rent: ")[1].strip()
        self.assertEqual(rent, "None")
