"""
Test Commands
"""
import os
from unittest import mock

from django.test import TestCase

from ..management.commands import (current_rent, fetch, lease_rent,
                                   list_rentals, store, tenant_masts)


class TestCommands(TestCase):
    "Test cases for commands"

    def _mock_parser(self):
        class MockParser:
            def __init__(self):
                self.args = None
                self.kwargs = None

            def add_argument(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs

        return MockParser()

    @mock.patch("apps.bink.functions.fetch.fetch")
    def test_fetch(self, mock):
        command = fetch.Command()
        parser = self._mock_parser()
        command.add_arguments(parser)
        self.assertNotEqual(parser.args, None)
        self.assertNotEqual(parser.kwargs, None)
        self.assertEqual(command.handle(url=None), None)

    @mock.patch("apps.bink.functions.store.store")
    def test_store(self, mock):
        command = store.Command()
        parser = self._mock_parser()
        command.add_arguments(parser)
        self.assertNotEqual(parser.args, None)
        self.assertNotEqual(parser.kwargs, None)
        self.assertEqual(command.handle(csv_file=None), None)

    def test_store_check_path(self):
        with self.assertRaises(store.argparse.ArgumentTypeError):
            store._check_path("--invalid--")

        self.assertEqual(os.path.abspath(__file__), store._check_path(__file__))

    @mock.patch("apps.bink.functions.lease_rent.lease_rent")
    def test_lease_rent(self, mock):
        command = lease_rent.Command()
        parser = self._mock_parser()
        command.add_arguments(parser)
        self.assertNotEqual(parser.args, None)
        self.assertNotEqual(parser.kwargs, None)
        self.assertEqual(command.handle(years=None), None)

    @mock.patch("apps.bink.functions.current_rent.current_rent")
    def test_current_rent(self, mock):
        command = current_rent.Command()
        parser = self._mock_parser()
        command.add_arguments(parser)
        self.assertNotEqual(parser.args, None)
        self.assertNotEqual(parser.kwargs, None)
        self.assertEqual(command.handle(max=None), None)

    @mock.patch("apps.bink.functions.list_rentals.list_rentals")
    def test_list_rentals(self, mock):
        command = list_rentals.Command()
        parser = self._mock_parser()
        command.add_arguments(parser)
        self.assertNotEqual(parser.args, None)
        self.assertNotEqual(parser.kwargs, None)
        self.assertEqual(command.handle(**{"from": None, "till": None}), None)

    def test_list_rentals_check_date(self):
        with self.assertRaises(store.argparse.ArgumentTypeError):
            list_rentals._check_date("--invalid--")

        self.assertEqual("01-01-1999", list_rentals._check_date("1-1-1999"))

    @mock.patch("apps.bink.functions.tenant_masts.tenant_masts")
    def test_tenant_masts(self, mock):
        command = tenant_masts.Command()
        self.assertEqual(command.handle(), None)
