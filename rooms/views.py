from django.core import paginator
from django.shortcuts import render
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.permissions import IsOwner
from rooms.serializers import RoomCreateSerializer, RoomSerializer

from .models import Room


class CustomPagination(PageNumberPagination):
    page_size = 10


# class RoomView(APIView):
#     def get_object(self, pk):
#         try:
#             room = Room.objects.get(pk=pk)
#             return room
#         except Room.DoesNotExist:
#             return None

#     def get(self, request, pk=None):
#         room = self.get_object(pk)
#         if room is not None:
#             serializer = RoomSerializer(room).data
#             return Response(serializer)
#         else:
#             return Response({"error": "No room found"}, status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk=None):
#         room = self.get_object(pk)
#         if room is not None:
#             if room.user != request.user:
#                 return Response(
#                     {"message": "Sorry! You are not authorized to delete this content"},
#                     status=status.HTTP_403_FORBIDDEN,
#                 )
#             serializer = RoomCreateSerializer(room, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             return Response({"success": "Update!!"})
#         else:
#             return Response({"error": "No room found"}, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk=None):
#         room = self.get_object(pk)

#         if room is not None:
#             if room.user != request.user:
#                 return Response(
#                     {"message": "Sorry! You are not authorized to delete this content"},
#                     status=status.HTTP_403_FORBIDDEN,
#                 )
#             room.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response({"error": "No room found"}, status=status.HTTP_404_NOT_FOUND)


# @api_view(["GET", "POST"])
# def rooms_view(request):
#     if request.method == "GET":
#         paginator = CustomPagination()
#         rooms = Room.objects.all()
#         results = paginator.paginate_queryset(rooms, request)
#         serializer = RoomSerializer(results, many=True, context={"request": request})
#         return paginator.get_paginated_response(serializer.data)
#     elif request.method == "POST":
#         if not request.user.is_authenticated:
#             return Response({"error": "Unauthorized User"}, status=status.HTTP_401_UNAUTHORIZED)
#         serializer = RoomCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             room = serializer.save(user=request.user)
#             room_serializer = RoomSerializer(room)
#             return Response(
#                 {"success": "Room Created sucessfully", "data": room_serializer.data}, status=status.HTTP_201_CREATED
#             )
#         else:
#             return Response(
#                 {"error": "something went wrong"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


class RoomViewSets(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    @action(detail=False)
    def search(self, request):
        max_price = request.GET.get("max_price", None)
        min_price = request.GET.get("min_price", None)
        beds = request.GET.get("beds", None)
        bedrooms = request.GET.get("bathrooms", None)
        bathrooms = request.GET.get("bathrooms", None)
        name = request.GET.get("name", None)
        lat = request.GET.get("lat", None)
        lng = request.GET.get("lng", None)

        filter_kwargs = {}

        if max_price is not None:
            filter_kwargs["price__lte"] = max_price
        if min_price is not None:
            filter_kwargs["price__gte"] = min_price

        if beds is not None:
            filter_kwargs["beds__gte"] = beds
        if bedrooms is not None:
            filter_kwargs["bedrooms__gte"] = bedrooms
        if bathrooms is not None:
            filter_kwargs["bathrooms__gte"] = bathrooms
        if name is not None:
            filter_kwargs["name__icontains"] = name
        if lat is not None and lng is not None:
            filter_kwargs["lat__gte"] = float(lat) - 0.005
            filter_kwargs["lat__lte"] = float(lat) + 0.005
            filter_kwargs["lng__gte"] = float(lng) - 0.005
            filter_kwargs["lng__lte"] = float(lng) + 0.005

        paginator = self.paginator
        try:
            rooms = Room.objects.filter(**filter_kwargs)
        except ValueError:
            rooms = Room.objects.all()
        results = paginator.paginate_queryset(rooms, request)
        serializers = RoomSerializer(results, many=True)

        return paginator.get_paginated_response(serializers.data)
