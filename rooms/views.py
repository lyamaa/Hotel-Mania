from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.serializers import RoomCreateSerializer, RoomDetailSerializer, RoomSerializer

from .models import Room


class ListRooms(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomView(APIView):
    def get_object(self, pk):
        try:
            room = Room.objects.get(pk=pk)
            return room
        except Room.DoesNotExist:
            return None

    def get(self, request, pk=None):
        room = self.get_object(pk)
        if room is not None:
            serializer = RoomSerializer(room).data
            return Response(serializer)
        else:
            return Response({"error": "No room found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        room = self.get_object(pk)
        if room is not None:
            if room.user != request.user:
                return Response(
                    {"message": "Sorry! You are not authorized to delete this content"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            serializer = RoomCreateSerializer(room, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success": "Update!!"})
        else:
            return Response({"error": "No room found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        room = self.get_object(pk)

        if room is not None:
            if room.user != request.user:
                return Response(
                    {"message": "Sorry! You are not authorized to delete this content"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "No room found"}, status=status.HTTP_404_NOT_FOUND)


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
