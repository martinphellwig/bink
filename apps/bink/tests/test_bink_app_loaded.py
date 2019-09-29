"""
Test if the bink app is loaded by django
"""

from django.apps import apps
from django.test import TestCase

from ..apps import BinkConfig


class TestAppLoaded(TestCase):
    "Sanity check for the app"

    def test_app_loaded(self):
        "Is the app available in Django?"
        from_django = apps.get_app_config("bink")
        self.assertEqual("apps." + BinkConfig.name, from_django.name)
