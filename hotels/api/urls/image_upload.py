from django.urls import path
from django.urls.conf import include

from hotels.api.views.views import ImageUpload

urlpatterns = [path("upload", ImageUpload.as_view())]
