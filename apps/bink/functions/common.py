"""
Common functionality
"""
from csv import writer
from io import StringIO

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

MAP_FIELDS_R = {value: key for key, value in MAP_FIELDS.items()}


def _make_row(instance):
    row = []

    for model, attribute in MAP_FIELDS.values():
        if model == "Unit":
            fetch_instance = instance
        else:
            name = model.lower()
            if name == "unittype":
                name = "unit_type"
            fetch_instance = getattr(instance, name)

        value = getattr(fetch_instance, attribute)
        row.append(value)

    return row


def make_csv_from_unit_queryset(queryset):
    "Take a unit queryset and return a csv text output."
    file_like_object = StringIO()
    csv = writer(file_like_object)
    csv.writerow(MAP_FIELDS.keys())

    for instance in queryset:
        row = _make_row(instance)
        csv.writerow(row)

    return file_like_object.getvalue()
