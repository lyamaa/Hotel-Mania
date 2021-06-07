from rest_framework_extensions.routers import ExtendedDefaultRouter

from hotels.api.views.views import (
    HotelViewSets,
    HotelSpecificationValuesViewSets,
    HotelTypeViewSets,
    HotelSpecificationViewSets,
)

router = ExtendedDefaultRouter()

urlpatterns = []

# urlpatterns += [
#     path("", include("hotels.api.urls.hotel_specification")),
#     path("", include("hotels.api.urls.image_upload")),
# ]


router.register("hotels/", HotelViewSets, basename="hotel")
router.register(
    "hotels/specs/",
    HotelSpecificationViewSets,
    basename="h-spec",
)
router.register(
    "hotels/specs/value",
    HotelSpecificationValuesViewSets,
    basename="h-spec-value",
)
router.register("hotel-types", HotelTypeViewSets, basename="h-type")

urlpatterns += router.urls
