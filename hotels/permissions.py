from rest_framework.permissions import BasePermission


class IsHotelOwner(BasePermission):
    def has_object_permission(self, request, view, hotel):
        return hotel.hotel_owner == request.user
