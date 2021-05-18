from django.urls import path

from .views import RoomView, rooms_view

app_name = "rooms"

urlpatterns = [path("", rooms_view), path("<int:pk>/", RoomView.as_view())]
