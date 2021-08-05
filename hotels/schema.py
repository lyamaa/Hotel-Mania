import graphene
from graphene_django import DjangoObjectType
from .models import Hotel


class HotelType(DjangoObjectType):
    class Meta:
        model = Hotel


