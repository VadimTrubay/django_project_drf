from rest_framework import generics

from .models import Image
from .serializers import ImageSerializer


class ImageListApiView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRetrieveApiView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageCreateApiView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageUpdateApiView(generics.UpdateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDeleteApiView(generics.DestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

