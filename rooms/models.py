from django.utils import module_loading
from commons.models import ConfigChoice
from django.db import models
from core.models import CoreModel
from django.utils.translation import gettext_lazy as _


class Room(CoreModel):
    hotel = models.ForeignKey("hotels.Hotel", on_delete=models.CASCADE)
    room_tag = models.IntegerField(_("Room Tag"), default=100)
    name = models.CharField(
        _("Room Name"),
        max_length=255,
    )
    image = models.URLField(max_length=255, null=True)
    capacity = models.IntegerField(default=0)
    price = models.DecimalField(
        help_text="RS per night", decimal_places=2, max_digits=10
    )
    beds = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    instant_book = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Service_spec(models.Model):
    title = models.CharField(_("Service Title"), max_length=255)
    description = models.TextField(_("Service Description"))

    def __str__(self) -> str:
        return self.title


class RoomService(models.Model):
    service_name = models.CharField(_("Service Name"), max_length=255)
    service_type = models.ManyToManyField(Service_spec)
    description = models.TextField(
        _("Service Description"), max_length=255, null=True, blank=True
    )
    hotel = models.ForeignKey(
        "hotels.Hotel", verbose_name=_("Hotel"), on_delete=models.CASCADE
    )
    room = models.ForeignKey(Room, verbose_name=_("Room"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.service_name
