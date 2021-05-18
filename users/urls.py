from django.urls import path

from .views import FavsView, MeView, UsersView, user_detail

app_name = "users"

urlpatterns = [
    path("", UsersView.as_view()),
    path("me/", MeView.as_view()),
    path("me/favs/", FavsView.as_view()),
    path("<int:pk>/", user_detail),
]
