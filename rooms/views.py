from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from rooms.serializers import RoomDetailSerializer, RoomSerializer

from .models import Room


class ListRooms(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
