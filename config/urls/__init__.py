from django.urls import path, include


urlpatterns = [
    path("dj-admin/", include("config.urls.dj-admin")),
    path("api/v1/", include("config.urls.hotel")),
]
