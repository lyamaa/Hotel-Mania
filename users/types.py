from graphene_django import DjangoObjectType
import graphene
from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "last_login",
            "is_staff",
            "is_active",
            "superhost",
        )
