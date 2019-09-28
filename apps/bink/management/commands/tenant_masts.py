"""
This command implements requirements 3
"""
from django.core.management.base import BaseCommand

from ...functions import tenant_masts


class Command(BaseCommand):
    "Django Command; `lease_rent`."
    help = """
    Returns a dictionary of tenants and mast count.
    """

    def handle(self, *args, **options):
        tenant_masts.tenant_masts()
