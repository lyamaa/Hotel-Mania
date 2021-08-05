from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from config.schema import schema

urlpatterns = [
    path("dj-admin/", include("config.urls.dj-admin")),
    path("api/v1/hotel/", include("config.urls.hotel")),
    path("api/v1/common/", include("config.urls.common")),
    path("api/v1/", include("config.urls.room")),
    path("api/v2/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
