"Django Admin module."
from django.contrib import admin

from . import models

admin.site.register(models.Lease)
admin.site.register(models.Property)
admin.site.register(models.Tenant)
admin.site.register(models.Unit)
admin.site.register(models.UnitType)
