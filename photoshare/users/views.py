from rest_framework import generics

from django.contrib.auth.models import User
from .models import Profile
from .serializers import *


# class UserEditApiView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class ProfileApiView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileEditApiView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDeleteApiView(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer