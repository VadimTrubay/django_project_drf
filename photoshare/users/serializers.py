from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username',)

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'profile_picture', 'first_name', 'last_name', 'email', 'phone')
