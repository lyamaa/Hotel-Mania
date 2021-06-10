from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import Room, RoomService


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.StringRelatedField()

    class Meta:
        model = Room
        fields = (
            "id",
            "hotel",
            "name",
            "price",
            "image",
            "beds",
            "bedrooms",
            "bathrooms",
            "capacity",
        )


class RoomServiceSerializer(serializers.ModelSerializer):
    service_type = serializers.StringRelatedField()
    hotel = serializers.StringRelatedField()
    room = serializers.StringRelatedField()

    class Meta:
        model = RoomService
        fields = (
            "id",
            "service_name",
            "service_type",
            "description",
            "hotel",
            "room",
        )
