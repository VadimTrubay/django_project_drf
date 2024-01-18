from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import *
from .models import Item

class AllItemsViewSet(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = AllItemSerializer
    # permission_classes = [IsAuthenticated]

    # def get_permissions(self):  #  PROBLEM USER ADMIN OR USER
    #     self.permission_classes = [IsAuthenticated]
    #     self.queryset = Item.objects.filter(user=self.request.user)
    #     return super().get_permissions()


class AddItemViewSet(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = AddItemSerializer
    # permission_classes = [IsAuthenticated]


class ViewItemViewSet(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ViewItemSerializer
    # permission_classes = [IsAuthenticated]


class EditItemViewSet(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = EditItemSerializer
    # permission_classes = [IsAuthenticated]


class DeleteItemViewSet(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = DeleteItemSerializer
    # permission_classes = [IsAuthenticated]
