"""
This module contains the store function which is used in the django command
store function.
"""
import csv

from django.utils.timezone import datetime

from .. import models

_INSTANCE_CACHE = {}

MAP_FIELDS = {
    "Units Reference": ("Unit", "reference"),
    "Unit Name": ("Unit", "name"),
    "Tenant Name": ("Tenant", "name"),
    "Property Name": ("Property", "name"),
    "Property Address": ("Property", "address"),
    "Lease Start Date": ("Lease", "started"),
    "Lease End Date": ("Lease", "stopped"),
    "Lease Years": ("Lease", "years"),
    "Next Rent Review": ("Lease", "review"),
    "Current Rent": ("Lease", "rent"),
    "Unit type": ("UnitType", "value"),
}

MAP_FIELD_R = {value: key for key, value in MAP_FIELDS.items()}


def _save_instance_cached(model_name, data):
    "Cached saving of an instance."
    # Many values are duplicates, if we detect this we return the cached one
    # instead.
    key_values = list(data.items())
    key_values.sort()
    key_values = tuple(key_values)
    key = (model_name, key_values)

    if key not in _INSTANCE_CACHE:
        model = getattr(models, model_name)
        values = {key[1]: value for key, value in data.items()}
        instance = model.objects.get_or_create(**values)[0]

        _INSTANCE_CACHE[key] = instance

    return _INSTANCE_CACHE[key]


_DATE_KEYS = [("Lease", "started"), ("Lease", "stopped"), ("Lease", "review")]


def _save_instance(fields, row):
    "Save each value instance."
    # Go through each field, sanitize where necessary and save it to the db.
    model_name = fields[0][0]
    data = {}

    for instance_field in fields:
        item_key = MAP_FIELD_R[instance_field]
        item = row[item_key]

        # Sanitize values
        if instance_field in _DATE_KEYS:
            item = item.strip()
            if item == "":
                item = None
            elif "/" in item:
                item = None
            else:
                item = datetime.strptime(item, "%d-%b-%y")
                item = item.date().isoformat()

        if instance_field == ("Lease", "rent"):
            if "." not in item:
                item += ".00"

        if instance_field == ("Lease", "years"):
            item = item.strip()
            if item == "":
                item = None

        data[instance_field] = item

    return _save_instance_cached(model_name, data)


def _store_row(row):
    "Store each row in the database."
    # Save each referred instance and then finally save the unit with all its
    # references.
    unit_kwargs = {}
    unit_kwargs["tenant"] = _save_instance(fields=[("Tenant", "name")], row=row)

    unit_kwargs["property"] = _save_instance(
        fields=[("Property", "name"), ("Property", "address")], row=row
    )

    unit_kwargs["lease"] = _save_instance(
        fields=[
            ("Lease", "started"),
            ("Lease", "stopped"),
            ("Lease", "years"),
            ("Lease", "review"),
            ("Lease", "rent"),
        ],
        row=row,
    )

    unit_kwargs["unit_type"] = _save_instance(fields=[("UnitType", "value")], row=row)

    unit_kwargs["reference"] = row["Units Reference"]
    unit_kwargs["name"] = row["Unit Name"]

    models.Unit.objects.create(**unit_kwargs)


def store(filename):
    "Store the contents of the file in the DB."
    with open(filename, "r") as file_read:
        reader = csv.DictReader(file_read)

        # Sanity check the CSV file
        if reader.fieldnames != list(MAP_FIELDS.keys()):
            text = "Format of CSV changed, please adjust the field mapping."
            raise ValueError(text)

        # Empty the DB.
        defined_models = [
            models.Lease,
            models.Property,
            models.Tenant,
            models.Unit,
            models.UnitType,
        ]
        for model in defined_models:
            model.objects.all().delete()

        # Empty cache
        _INSTANCE_CACHE.clear()

        # Populate the DB
        for row in reader:
            _store_row(row)
