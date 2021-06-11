from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import Room, RoomService, Service_spec


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


class ServiceSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_spec
        fields = "__all__"


class ServiceRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return ServiceSpecSerializer(value).data

    def to_internal_value(self, data):
        return data


class RoomServiceSerializer(serializers.ModelSerializer):
    service_type = ServiceRelatedField(many=True)
    # hotel = serializers.StringRelatedField()
    # room = serializers.StringRelatedField()

    class Meta:
        model = RoomService
        fields = "__all__"

    def create(self, validated_data):
        service_type = validated_data.pop("service_type", None)
        instance = self.Meta.model(**validated_data)
        instance.save()
        instance.service_type.add(*service_type)
        instance.save()
        return instance
