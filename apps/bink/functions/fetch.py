"""
This module contains the fetch function which is used in the django command
fetch function.
"""
import csv
from io import StringIO

import requests
from django.core.management.base import CommandError

DEFAULT_LOCATION = (
    "https://datamillnorth.org/download/mobile-phone-masts/"
    "f027f462-3621-4dba-8917-dc35d70a0fb2/"
    "Mobile%2520Phone%2520Masts%252001.04.2019a.csv"
)


def fetch(url=DEFAULT_LOCATION):
    "Fetch CSV from url and print to stdout."
    response = None

    response = requests.get(url)
    if response.status_code != 200:
        error_text = "Status code '{}' raised for url '{}'.".format(
            response.status_code, url
        )
        raise CommandError(error_text)

    # Lets open the content and write it back so we are sure we have a valid
    # csv, since the data is not that large lets do it in memory and save on
    # having to handle temporary files.
    file_like_object = StringIO()
    writer = csv.writer(file_like_object)

    try:
        reader = csv.reader(response.text.splitlines())
        for row in reader:
            writer.writerow(row)

    except (ValueError, csv.Error):
        error_text = "Downloaded content is not valid CSV; url '{}'.".format(url)
        raise CommandError(error_text)

    print(file_like_object.getvalue())
