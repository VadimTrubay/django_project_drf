from rest_framework import generics

from .models import Tag
from .serializers import TagSerializer


class TagListApiView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveApiView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagCreateApiView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagUpdateApiView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDeleteApiView(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer