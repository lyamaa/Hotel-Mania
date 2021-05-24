from django.db import models
from drf_writable_nested import WritableNestedModelSerializer
from hotels.models import (
    Hotel,
    HotelImage,
    HotelSpecifications,
    HotelSpecificationValue,
    HotelType,
)
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = "__all__"


class HotelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelType
        fields = "__all__"


class HotelSpecificationSerilaizer(WritableNestedModelSerializer):
    hotel_type = HotelTypeSerializer()

    class Meta:
        model = HotelSpecifications
        fields = "__all__"


class Hotelserializer(serializers.ModelSerializer):
    # config_choice = serializers.StringRelatedField()
    # hotel_type = serializers.StringRelatedField()
    hotel_owner = serializers.StringRelatedField()
    hotel_type = HotelTypeSerializer()

    class Meta:
        model = Hotel
        exclude = ("is_active", "created", "modified")


class HotelSpecificationValueSerializer(serializers.ModelSerializer):
    hotel = Hotelserializer()
    specification = HotelSpecificationSerilaizer()

    class Meta:
        model = HotelSpecificationValue
        fields = "__all__"
