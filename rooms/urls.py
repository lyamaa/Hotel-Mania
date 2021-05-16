from django.urls import path

from .views import RoomDetailView, rooms_view

app_name = "rooms"

urlpatterns = [path("", rooms_view), path("<int:pk>/", RoomDetailView.as_view())]
