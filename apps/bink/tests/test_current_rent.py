"""
Test Cases for Current Rent
"""
from io import StringIO

from django.test import TestCase

from ..functions import current_rent
from .factories import UnitFactory, reset


class TestCurrentRent(TestCase):
    "Test cases for fetch"

    def test_1_returns_current_rent(self):
        "Is the output equal to what we put in?"
        lease_years = 2
        reset()
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
            "unit 0\r\n\n"
        )
        output = StringIO()
        current_rent.current_rent(lease_years, output)
        returned = output.getvalue()
        self.assertEqual(returned, expected)
