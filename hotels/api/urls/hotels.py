from django.urls import path
from rest_framework.routers import DefaultRouter

from ..views.views import HotelViewSets

app_name = "hotel"
router = DefaultRouter()
router.register("hotels/", HotelViewSets)


urlpatterns = router.urls
