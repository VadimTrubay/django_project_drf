from rest_framework import generics

from .models import Comment
from .serializers import CommentSerializer


class CommentListApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveApiView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateApiView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateApiView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDeleteApiView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

