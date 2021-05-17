from django.urls import path

from .views import HotelListView

app_name = "hotel"

urlpatterns = [path("", HotelListView.as_view(), name="hotels")]
