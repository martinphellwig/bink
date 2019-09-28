"""
Test Cases for fetch
"""
import os

from django.test import TestCase

from .. import models
from ..functions import store

DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(DIR, "_test_data_small.csv")
TEST_DATA_INVALID_FIELD = os.path.join(DIR, "_test_data_invalid_field_name.csv")
TEST_DATA_EMPTY_FIELD = os.path.join(DIR, "_test_data_empty_fields.csv")


class TestStore(TestCase):
    "Test cases for fetch"

    def test_1_stores_small_sheet(self):
        "Does it raise a command error on a 404."
        first_count = models.Unit.objects.all().count()
        store.store(TEST_DATA)
        second_count = models.Unit.objects.all().count()
        self.assertGreater(second_count, first_count)

    def test_2_invalid_field_name(self):
        "Does it raise a command error on a 404."
        with self.assertRaises(ValueError):
            store.store(TEST_DATA_INVALID_FIELD)

    def test_3_stores_allowed_empty_fields_sheet(self):
        "Does it raise a command error on a 404."
        first_count = models.Unit.objects.all().count()
        store.store(TEST_DATA_EMPTY_FIELD)
        second_count = models.Unit.objects.all().count()
        self.assertGreater(second_count, first_count)
