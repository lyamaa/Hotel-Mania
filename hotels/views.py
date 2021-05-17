from rest_framework import generics

from hotels.models import Hotel

from .serializers import Hotelserializer


class HotelListView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = Hotelserializer
