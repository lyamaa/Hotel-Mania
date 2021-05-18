from rest_framework import fields, serializers
from users.serializer import UserSerializer

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Room
        exclude = ("modified",)


class RoomCreateSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Room
        fields = "__all__"

    def create(serlf, validated_data):
        return Room.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.price = validated_data.get("price", instance.price)
        instance.beds = validated_data.get("beds", instance.price)
        instance.lat = validated_data.get("lat", instance.lat)
        instance.lng = validated_data.get("lng", instance.lng)
        instance.bedrooms = validated_data.get("bedrooms", instance.bedrooms)
        instance.bathrooms = validated_data.get("bathrooms", instance.bathrooms)
        instance.check_in = validated_data.get("check_in", instance.check_in)
        instance.check_out = validated_data.get("check_out", instance.check_out)
        instance.instant_book = validated_data.get("instant_book", instance.instant_book)
        instance.user = validated_data.get("user", instance.user)

        instance.save()
        return instance


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
