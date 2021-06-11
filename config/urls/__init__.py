from django.urls import path, include


urlpatterns = [
    path("dj-admin/", include("config.urls.dj-admin")),
    path("api/v1/hotel/", include("config.urls.hotel")),
    path("api/v1/common/", include("config.urls.common")),
    path("api/v1/", include("config.urls.room")),
]
