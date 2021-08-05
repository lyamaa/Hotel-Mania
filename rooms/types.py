from graphene_django import DjangoObjectType
import graphene
from rooms.models import Room


class RoomType(DjangoObjectType):
    hotel = graphene.Field("hotels.schema.HotelType")

    class Meta:
        model = Room
