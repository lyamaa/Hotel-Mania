from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from rooms.serializers import RoomCreateSerializer, RoomDetailSerializer, RoomSerializer

from .models import Room


class ListRooms(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer


@api_view(["GET", "POST"])
def rooms_view(request):
    if request.method == "GET":
        rooms = Room.objects.all()[:5]
        serializer = RoomSerializer(rooms, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)
    elif request.method == "POST":
        if not request.user.is_authenticated:
            return Response({"error": "Unauthorized User"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = RoomCreateSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=request.user)
            room_serializer = RoomSerializer(room)
            return Response(
                {"success": "Room Created sucessfully", "data": room_serializer.data}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"error": "something went wrong"},
                status=status.HTTP_400_BAD_REQUEST,
            )
