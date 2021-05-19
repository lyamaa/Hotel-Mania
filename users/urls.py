from django.db import router
from django.urls import path
from rest_framework import urlpatterns

# from .views import FavsView, MeView, UsersView, login, user_detail
from rest_framework.routers import DefaultRouter

from .views import UserViewSets

app_name = "users"

router = DefaultRouter()

router.register("", UserViewSets)

urlpatterns = router.urls

# urlpatterns = [
#     path("", UsersView.as_view()),
#     path("token/", login),
#     path("me/", MeView.as_view()),
#     path("me/favs/", FavsView.as_view()),
#     path("<int:pk>/", user_detail),
# ]
