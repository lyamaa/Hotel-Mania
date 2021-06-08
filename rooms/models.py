from django.db import models
from core.models import CoreModel


class Room(CoreModel):

    name = models.CharField(max_length=140)
    price = models.DecimalField(
        help_text="RS per night", decimal_places=2, max_digits=10
    )
    image = models.URLField(max_length=255, null=True)
    beds = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    check_in = models.TimeField(default="00:00:00")
    check_out = models.TimeField(default="00:00:00")
    instant_book = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )

    def __str__(self):
        return self.name
