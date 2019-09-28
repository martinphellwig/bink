"""
Test Cases for tenant masts
"""
from io import StringIO

from django.test import TestCase

from ..functions import tenant_masts
from .factories import UnitFactory


class TestTenantMasts(TestCase):
    "Test cases for tenant_masts"

    def test_1_pprint_dict(self):
        "Is the output equal to what we put in?"
        lease_years = 2
        UnitFactory(
            tenant__name="Test",
            lease__years=lease_years,
            lease__rent=42,
            lease__started=None,
            lease__stopped=None,
            lease__review=None,
        )
        expected = "{'Test': 1}\n"
        output = StringIO()

        tenant_masts.tenant_masts(output)
        self.assertEqual(output.getvalue(), expected)
