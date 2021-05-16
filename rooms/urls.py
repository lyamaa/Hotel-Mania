from django.urls import path

from .views import ListRooms, RoomDetailView

app_name = "rooms"

urlpatterns = [path("", ListRooms.as_view()), path("<int:pk>/", RoomDetailView.as_view())]
