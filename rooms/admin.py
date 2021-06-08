from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = ("name", "price")
    list_filter = ("name",)
    search_fields = ("name__startswith",)
    list_display_links = ("name", "price")
