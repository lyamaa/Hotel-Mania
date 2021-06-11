from rest_framework_extensions.routers import ExtendedDefaultRouter
from django.urls import path
from rooms.api.views import CustomRoomCreateAPI, RoomServiceListView

router = ExtendedDefaultRouter()

urlpatterns = [path("rooms", RoomServiceListView.as_view())]

# urlpatterns += [
#     path("", include("hotels.api.urls.hotel_specification")),
#     path("", include("hotels.api.urls.image_upload")),
# ]


router.register("custom-rooms", CustomRoomCreateAPI, basename="custom-room")


urlpatterns += router.urls
