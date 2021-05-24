from django.core.files.storage import default_storage
from hotels.models import Hotel, HotelSpecifications, HotelSpecificationValue, HotelType
from hotels.permissions import IsHotelOwner
from rest_framework import generics, permissions, status, viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.serializers import (
    Hotelserializer,
    HotelSpecificationSerilaizer,
    HotelSpecificationValueSerializer,
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


class HotelSpecificationValuesViewSets(viewsets.ModelViewSet):
    queryset = HotelSpecificationValue.objects.all()
    serializer_class = HotelSpecificationValueSerializer


class ImageUpload(APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    def post(self, request):

        # converts querydict to original dict
        images = dict((request.data).lists())["image"]

        arr = []
        for img in images:
            filename = default_storage.save(img.name, img)
            url = default_storage.url(filename)
            urls = "http://localhost:8000/media" + url
            arr.append(urls)

        return Response(
            {
                "status": "success",
                "url": arr,
            }
        )
