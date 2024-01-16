from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Image
from .serializers import ImageSerializer
from comments.models import Comment # noqa

from tags.models import Tag # noqa


class ImageViewSet(viewsets.ModelViewSet):
    # queryset = Image.objects.all() # noqa
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Image.objects.all()
        return Image.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def comments(self, request):
        comm = Comment.objects.all()
        return Response({'comments': [c.comment for c in comm]})

    @action(methods=['get'], detail=False)
    def tags(self, request, pk=None):
        tags = Tag.objects.all()
        return Response({'tags': [t.tag for t in tags]})

    @action(methods=['get'], detail=True)
    def comment(self, request, pk=None):
        comm = Comment.objects.get(pk=pk)
        return Response({'comment': comm.comment})

    @action(methods=['get'], detail=True)
    def tag(self, request, pk=None):
        t = Tag.objects.get(pk=pk)
        return Response({'tag': t.tag})