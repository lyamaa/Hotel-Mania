from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/commons/", include("commons.urls")),
    # Hotels urls
    path("api/v1/", include("hotels.api.urls.main")),
    # path("api/v1/", include("hotels.api.urls.hotel_types")),
    # path("api/v1/", include("hotels.api.urls.hotel_specification")),
    # path("api/v1/", include("hotels.api.urls.hotel_specification")),
    # path("api/v1/", include("hotels.api.urls.hotel_specification_value_serializer")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
