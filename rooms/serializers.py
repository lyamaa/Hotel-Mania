from rest_framework import fields, serializers
from users.serializer import UserSerializer

from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Room
        exclude = ("modified",)


class RoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
