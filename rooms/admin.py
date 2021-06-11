from django.contrib import admin
from django.utils import module_loading
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ("name", "price")
    list_filter = ("name",)
    search_fields = ("name__startswith",)
    list_display_links = ("name", "price")


admin.site.register(models.Service_spec)
admin.site.register(models.RoomService)
