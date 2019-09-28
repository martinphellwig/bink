"""
Models to hold the mobile phone mast datasets in a relational matter.
"""

from django.db import models


class Tenant(models.Model):
    "Tenant of the Unit"
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    "Location of the Unit"
    name = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Properties"
        unique_together = [["name", "address"]]

    def __str__(self):
        return "{}: {}".format(self.address, self.name)


class Lease(models.Model):
    "Unit Lease"
    started = models.DateField(null=True)
    stopped = models.DateField(null=True)
    years = models.PositiveIntegerField(null=True)
    review = models.DateField(null=True)
    rent = models.DecimalField(null=True, decimal_places=2, max_digits=8)

    class Meta:
        unique_together = [["started", "stopped", "years", "review", "rent"]]

    def __str__(self):
        return "{}:{}:{}".format(self.started, self.stopped, self.rent)


class UnitType(models.Model):
    "Unit Type, e.g. Antenna or Tele Comm"
    value = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.value


class Unit(models.Model):
    "The mobile phone mast"
    reference = models.CharField(max_length=16, unique=True)
    name = models.TextField()
    unit_type = models.ForeignKey(
        UnitType, verbose_name="type", on_delete=models.CASCADE
    )
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.name, self.reference)
