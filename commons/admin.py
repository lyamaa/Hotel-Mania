from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from leaflet.admin import LeafletGeoAdmin

from .models import (
    Address,
    CertificationType,
    Company,
    ConfigChoice,
    ConfigChoiceCategory,
)

admin.site.register(ConfigChoiceCategory, MPTTModelAdmin)
admin.site.register(ConfigChoice)


@admin.register(Address)
class AddressAdmin(LeafletGeoAdmin):
    list_display = ("id", "city", "street_1", "state", "zip_code", "country")


admin.site.register(CertificationType)
admin.site.register(Company)
