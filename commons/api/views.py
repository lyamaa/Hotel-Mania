from django.contrib.gis.geos import Point
from django.db.models.query import QuerySet
from geopy.geocoders import Nominatim
from commons.api.serializers import (
    AddressSerializer,
    CompanySerializer,
    ConfigChoiceCategorySerializer,
    ConfigChoiceSerializer,
    CertificationTypeSerializer,
)
from rest_framework import serializers, viewsets
from ..models import (
    Address,
    CertificationType,
    Company,
    ConfigChoice,
    ConfigChoiceCategory,
)


geolocator = Nominatim(user_agent="commons")


class ConfigChoiceCategoryViewsets(viewsets.ModelViewSet):
    queryset = ConfigChoiceCategory.objects.all()
    serializer_class = ConfigChoiceCategorySerializer

    def perform_create(self, serializer):
        serializer.save(entered_by=self.request.user)


class ConfigChoiceViewsets(viewsets.ModelViewSet):
    queryset = ConfigChoice.objects.all()
    serializer_class = ConfigChoiceSerializer

    def perform_create(self, serializer):
        serializer.save(entered_by=self.request.user)


class AddressViewsets(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        street_1 = serializer.initial_data["street_1"]
        address = serializer.initial_data["city"]
        state = serializer.initial_data["state"]
        country = serializer.initial_data["city"]

        data = [street_1, address, state, country]
        " ".join(data)

        g = geolocator.geocode(data)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)

    def perform_update(self, serializer):
        street_1 = serializer.initial_data["street_1"]
        address = serializer.initial_data["city"]
        state = serializer.initial_data["state"]
        country = serializer.initial_data["city"]

        data = [street_1, address, state, country]
        " ".join(data)

        g = geolocator.geocode(data)
        lat = g.latitude
        lng = g.longitude
        pnt = Point(lng, lat)
        print(pnt)
        serializer.save(location=pnt)


class CompanyViewSets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CertificationTypeViewsets(viewsets.ModelViewSet):
    queryset = CertificationType.objects.all()
    serializer_class = CertificationTypeSerializer
