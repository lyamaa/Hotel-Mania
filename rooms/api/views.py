from copy import error
from datetime import date, datetime, timedelta
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rooms.api.serializers import RoomSerializer, RoomServiceSerializer
from rest_framework import viewsets
from rest_framework import permissions, mixins
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from hotels.models import Hotel
from ..models import Room, RoomService
from commons.models import ConfigChoice


class RoomServiceListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = RoomService.objects.all()
    serializer_class = RoomServiceSerializer


class CustomRoomCreateAPI(viewsets.ViewSet, mixins.CreateModelMixin):
    """
    # Custom class to create room and service in a given quantity
    {
        "hotel_id" : 1,
        "room_tag" : 100,
        "room_name":  "Delux suite",
        "service_name": "Service for demo hotel",
        "service_type": [1, 3],
        "description": "dsdasdadasda",
        "image": "https://res.cloudinary.com/dazyxzm1e/image/upload/v1621743459/tagme/w4yt2d8qmbndvotmy0lp.jpg",
        "price" :  2000.00,
        "capacity": 4,
        "beds": 2,
        "bedrooms": 1,
        "bathrooms": 1,
        "quantity": 5
    }
    """

    def create(self, request, *args, **kwargs):
        errors = {}

        hotel = request.data["hotel_id"]
        if not hotel:
            errors["hotel"] = "Hotel is Required"
        room_tag = request.data["room_tag"]
        if not room_tag:
            errors["room_tag"] = "Room Tag is required"
        name = request.data["room_name"]
        if not name:
            errors["name"] = "Room name is required"
        service_name = request.data["service_name"]
        if not service_name:
            errors["service_name"] = "Service name is required"
        service_type = request.data["service_type"]
        if not service_type:
            errors["service_type"] = "Service Type is required"
        description = request.data["description"]
        if not description:
            errors["description"] = "Description is required"
        image = request.data["image"]
        if not image:
            errors["image"] = "image is required"
        price = request.data["price"]
        if not price:
            errors["price"] = "Price is required"
        capacity = request.data["capacity"]
        if not capacity:
            errors["capacity"] = "capacity is required"
        beds = request.data["beds"]
        if not beds:
            errors["beds"] = "beds is required"
        bedrooms = request.data["bedrooms"]
        if not bedrooms:
            errors["bedrooms"] = "bedrooms is required"
        bathrooms = request.data["bathrooms"]
        if not bathrooms:
            errors["bathrooms"] = "bathrooms is required"
        # check_in = request.data["check_in"]

        # check_out = request.data["checkout"]
        quantity = request.data["quantity"]
        if not quantity:
            errors["quantity"] = "quantity is required"

        if errors:
            raise ValidationError(errors)

        hotel = Hotel.objects.get(pk=hotel)
        last_room = Room.objects.filter(hotel=hotel).last()

        if last_room:
            start_num = room_tag + 1
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
                # check_in=datetime.strptime(check_in, "%Y-%m-%d"),
                # check_out=datetime.strptime(check_out, "%Y-%m-%d"),
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
            room_service_serializer.save()
        return Response({"status": True, "message": f"Created {quantity} rooms"})
