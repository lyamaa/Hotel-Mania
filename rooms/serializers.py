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


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
