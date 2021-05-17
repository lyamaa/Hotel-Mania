from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Address,
    CertificationType,
    Company,
    ConfigChoice,
    ConfigChoiceCategory,
)

admin.site.register(ConfigChoiceCategory, MPTTModelAdmin)
admin.site.register(ConfigChoice)
admin.site.register(Address)
admin.site.register(CertificationType)
admin.site.register(Company)
