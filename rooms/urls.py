from django.urls import path
from rest_framework import views
from rest_framework.routers import DefaultRouter

from .views import RoomViewSets

app_name = "rooms"


router = DefaultRouter()
router.register("", RoomViewSets)

urlpatterns = router.urls

# urlpatterns = [
#     path("search/", room_search),
# ]
