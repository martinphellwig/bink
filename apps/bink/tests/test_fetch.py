"""
Test Cases for fetch
"""
import os
from io import StringIO
from unittest import mock

from django.test import TestCase

from ..functions import fetch

DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA = os.path.join(DIR, "_test_data.csv")


def _mocked_requests(text=None, status_code=None):
    class Response:
        "Mocked Requests response"

        def __init__(self, url):
            self.url = url

            if isinstance(text, str) and os.path.exists(text):
                with open(text, "r") as file_read:
                    self.text = "".join(file_read.readlines())
            else:
                self.text = text

            self.status_code = status_code

        def raise_for_status(self):
            "dummy function"

        def close(self):
            "dummy function"

    def get(url):
        return Response(url)

    return get


class TestFetch(TestCase):
    "Test cases for fetch"

    @mock.patch("requests.get", side_effect=_mocked_requests("", 404))
    def test_1_raises_error_on_404(self, mock_get):
        "Does it raise a command error on a 404."
        with self.assertRaises(fetch.CommandError):
            fetch.fetch()
        self.assertTrue(mock_get.called)

    @mock.patch("sys.stdout", new_callable=StringIO)
    @mock.patch("requests.get", side_effect=_mocked_requests(TEST_DATA, 200))
    def test_2_parses_known_good_content(self, mock_get, mock_stdout):
        "Does it parse a known good content?"
        fetch.fetch()
        self.assertTrue(mock_get.called)
        container = mock_stdout.getvalue()
        member = "1235/001,Clyde Grange,CCTV,,LS12 1XP,,,,,30,Tele Comm"
        self.assertIn(member, container)

    @mock.patch("requests.get", side_effect=_mocked_requests(b"\x00", 200))
    def test_2_errors_on_bad_content(self, mock_get):
        "Does it raises on bad content?"
        with self.assertRaises(fetch.CommandError):
            fetch.fetch()
        self.assertTrue(mock_get.called)
