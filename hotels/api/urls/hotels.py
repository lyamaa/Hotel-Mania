from django.urls import path
from rest_framework.routers import DefaultRouter

from ..views.views import HotelTypeViewSets, HotelViewSets

app_name = "hotel"
router = DefaultRouter()
router.register("", HotelViewSets)
router.register("hotel-types", HotelTypeViewSets)


urlpatterns = router.urls
