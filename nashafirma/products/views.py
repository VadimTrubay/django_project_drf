from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import *


class AllProductsViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class AddProductViewSet(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer
    permission_classes = [IsAdminUser]


class ViewProductViewSet(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ViewProductSerializer
    permission_classes = [IsAdminUser]


class EditProductViewSet(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = EditProductSerializer
    permission_classes = [IsAdminUser]


class DeleteProductViewSet(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DeleteProductSerializer
    permission_classes = [IsAdminUser]
