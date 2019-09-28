"""
Test Cases for models
"""

from django.test import TestCase

from . import factories


class TestFetch(TestCase):
    "Test cases for models"

    def test_1_tenant_str(self):
        "Does it raise a command error on a 404."
        subject = factories.TenantFactory
        instance = subject()
        expected = instance.name
        returned = str(instance)
        self.assertEqual(expected, returned)

    def test_2_property_str(self):
        "Does it raise a command error on a 404."
        subject = factories.PropertyFactory
        instance = subject()
        expected = "{}: {}".format(instance.address, instance.name)
        returned = str(instance)
        self.assertEqual(expected, returned)

    def test_3_lease_str(self):
        "Does it raise a command error on a 404."
        subject = factories.LeaseFactory
        instance = subject()
        expected = "{}:{}:{}".format(instance.started, instance.stopped, instance.rent)
        returned = str(instance)
        self.assertEqual(expected, returned)

    def test_4_unittype_str(self):
        "Does it raise a command error on a 404."
        subject = factories.UnitTypeFactory
        instance = subject()
        expected = instance.value
        returned = str(instance)
        self.assertEqual(expected, returned)

    def test_5_unit_str(self):
        "Does it raise a command error on a 404."
        subject = factories.UnitFactory
        instance = subject()
        expected = "{} ({})".format(instance.name, instance.reference)
        returned = str(instance)
        self.assertEqual(expected, returned)
