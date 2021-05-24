from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("", include("hotels.api.urls.hotels", namespace="hotel")),
    path("", include("hotels.api.urls.hotel_types")),
    path("", include("hotels.api.urls.hotel_specification")),
    path("", include("hotels.api.urls.hotel_specification_value")),
    path("", include("hotels.api.urls.image_upload")),
]
