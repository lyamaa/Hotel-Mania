import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rooms.models import Room
from rooms.permissions import IsOwner
from rooms.serializers import RoomSerializer

from users.permissions import IsSelf
from users.serializer import UserSerializer

from .models import User


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif self.action == "create" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["POST"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "username and password cannot be wmpty"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode({"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256")
            return Response(data={"token": encoded_jwt, "id": user.pk})

        else:
            return Response({"error": "invalid Credentials provided"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True)
    def favs(self, request, pk=None):
        user = self.get_object()
        serializer = RoomSerializer(user.favs.all(), many=True).data
        return Response(serializer)

    @favs.mapping.put
    def toggle_favs(self, request, pk=None):
        pk = request.data.get("pk", None)
        user = self.get_object()
        if pk is not None:
            try:
                room = Room.objects.get(pk=pk)
                if room in user.favs.all():
                    user.favs.remove(room)
                    return Response({"message": "Rooms Removed to ur favourites"})
                else:
                    user.favs.add(room)
                    return Response({"message": "Rooms added to ur favourites"})

            except Room.DoesNotExist:
                pass
        return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


# class UsersView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             new_user = serializer.save()
#             user_serializer = UserSerializer(new_user)

#             return Response(user_serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     if not username or not password:
#         return Response({"error": "username and password cannot be wmpty"}, status=status.HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         encoded_jwt = jwt.encode({"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256")
#         return Response(data={"token": encoded_jwt})

#     else:
#         return Response({"error": "invalid Credentials provided"}, status=status.HTTP_401_UNAUTHORIZED)


# class MeView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response(ReadUserSerializer(request.user).data)

#     def put(self, request):
#         serializer = WriteUserSerializer(request.user, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response()
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET"])
# def user_detail(request, pk=None):
#     try:
#         user = User.objects.get(pk=pk)
#         return Response(ReadUserSerializer(user).data)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# class FavsView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user
#         serializer = RoomSerializer(user.favs.all(), many=True).data
#         return Response(serializer)

#     def put(self, request):
#         pk = request.data.get("pk", None)
#         user = request.user
#         if pk is not None:
#             try:
#                 room = Room.objects.get(pk=pk)
#                 if room in user.favs.all():
#                     user.favs.remove(room)
#                     return Response({"message": "Rooms Removed to ur favourites"})
#                 else:
#                     user.favs.add(room)
#                     return Response({"message": "Rooms added to ur favourites"})

#             except Room.DoesNotExist:
#                 pass
#         return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
