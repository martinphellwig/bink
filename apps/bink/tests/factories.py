"""
Factories as used by factory boy.
"""
import datetime

import factory
import factory.fuzzy

from .. import models


class TenantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tenant

    name = factory.Sequence(lambda sequence: "Tenant Name #{}".format(sequence))


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Property

    name = factory.Sequence(lambda sequence: "Property Name #{}".format(sequence))
    address = factory.Sequence(lambda sequence: "XYZ {}AB".format(sequence))


class LeaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Lease

    started = factory.fuzzy.FuzzyDate(
        datetime.date(2001, 1, 1), datetime.date(2004, 1, 1)
    )
    stopped = factory.fuzzy.FuzzyDate(
        datetime.date(2005, 1, 1), datetime.date(2008, 1, 1)
    )
    years = factory.sequence(lambda sequence: sequence)
    review = factory.fuzzy.FuzzyDate(
        datetime.date(2002, 1, 1), datetime.date(2007, 1, 1)
    )
    rent = factory.sequence(lambda sequence: sequence)


class UnitTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.UnitType

    value = factory.Sequence(lambda sequence: "unit {}".format(sequence))


class UnitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Unit

    reference = factory.Sequence(lambda sequence: "ref/{}".format(sequence))
    name = factory.Sequence(lambda sequence: "Unit {}".format(sequence))
    unit_type = factory.SubFactory(UnitTypeFactory)
    tenant = factory.SubFactory(TenantFactory)
    property = factory.SubFactory(PropertyFactory)
    lease = factory.SubFactory(LeaseFactory)


def reset():
    factories = [
        TenantFactory,
        PropertyFactory,
        LeaseFactory,
        UnitTypeFactory,
        UnitFactory,
    ]
    for factory in factories:
        factory.reset_sequence()
