from datetime import date, datetime, timedelta
from rooms.api.serializers import RoomServiceSerializer
from rest_framework import viewsets
from rest_framework import permissions, mixins
from rest_framework.response import Response

from hotels.models import Hotel
from ..models import Room


class CustomRoomCreateAPI(viewsets.ViewSet, mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        hotel = request.data["hotel_id"]
        room_tag = request.data["room_tag"]
        name = request.data["room_name"]
        service_name = request.data["service_name"]
        service_type = request.data["service_type"]
        description = request.data["description"]
        image = request.data["image"]
        price = request.data["price"]
        capacity = request.data["capacity"]
        beds = request.data["beds"]
        bedrooms = request.data["bedrooms"]
        bathrooms = request.data["bathrooms"]
        check_in = request.data["check_in"]
        check_out = request.data["checkout"]
        quantity = request.data["quantity"]

        hotel = Hotel.objects.get(id=hotel)
        last_room = Room.objects.filter(hotel=hotel).last()

        if last_room:
            start_num = room_tag[-1] + 1
        else:
            start_num = 100
        end_num = start_num + quantity

        for tag in range(start_num, end_num):
            room = Room.objects.create(
                hotel=hotel,
                room_tag=tag,
                name=name,
                image=image,
                price=price,
                capacity=capacity,
                beds=beds,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                check_in=datetime.strptime(check_in, "%Y-%m-%d"),
                check_out=datetime.strptime(check_out, "%Y-%m-%d"),
            )
            room_service_serializer = RoomServiceSerializer(
                data={
                    "service_name": service_name,
                    "service_type": service_type,
                    "description": description,
                    "hotel": hotel.pk,
                    "room": room.pk,
                }
            )
            room_service_serializer.is_valid(raise_exception=True)
            service_type = room_service_serializer.save()
        return Response({"status": True, "message": f"Created {quantity} rooms"})
