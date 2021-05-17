from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Hotel, HotelImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = "__all__"


class Hotelserializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    hotel_type = serializers.StringRelatedField()

    class Meta:
        model = Hotel
        fields = ("id", "slug", "name", "description", "config_choice", "hotel_type", "get_absolute_url")
