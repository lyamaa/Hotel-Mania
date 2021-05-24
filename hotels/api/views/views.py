from hotels.models import Hotel, HotelSpecifications, HotelType
from hotels.permissions import IsHotelOwner
from rest_framework import generics, permissions, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..serializers.serializers import (
    Hotelserializer,
    HotelSpecificationSerilaizer,
    HotelTypeSerializer,
)


class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = Hotelserializer


class HotelViewSets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = Hotelserializer

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsHotelOwner]
        return [permission() for permission in permission_classes]


class HotelTypeViewSets(viewsets.ModelViewSet):
    queryset = HotelType.objects.all()
    serializer_class = HotelTypeSerializer


class HotelSpecificationViewSets(viewsets.ModelViewSet):
    queryset = HotelSpecifications.objects.all()
    serializer_class = HotelSpecificationSerilaizer
