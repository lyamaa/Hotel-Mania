import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decoded.get("pk")
            print(pk)
            user = User.objects.get(pk=pk)
            print("USER IS", user)

            return (user, None)
        except ValueError:
            raise exceptions.AuthenticationFailed("No such user")
