from django.urls import path
from rest_framework.routers import DefaultRouter

from ..views.views import HotelSpecificationViewSets

router = DefaultRouter()

router.register("hotel-specifications", HotelSpecificationViewSets)


urlpatterns = router.urls
