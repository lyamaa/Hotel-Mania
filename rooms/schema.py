import graphene

from .models import Room
from .types import RoomType


class Query(object):
    rooms = graphene.List(RoomType, page=graphene.Int())
    total = graphene.Int()
    room = graphene.Field(RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        if page < 1:
            page = 1
        page_size = 5
        skip = page_size * (page - 1)
        taking = page_size * page
        room_list = Room.objects.select_related("hotel").all()[skip:taking]
        print(room_list)

        return room_list

    def resolve_total(self, info):
        total = Room.objects.count()
        return total

    def resolve_room(self, info, id):
        try:
            return Room.objects.select_related('hotel').get(id=id)
        except Room.DoesNotExist:
            return None
