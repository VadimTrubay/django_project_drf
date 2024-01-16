from rest_framework import generics, viewsets

from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Profile
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
