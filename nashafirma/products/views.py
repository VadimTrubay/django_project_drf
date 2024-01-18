from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class AllProductsViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = AllProductsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Product.objects.all()
        return Product.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def product(self, request, pk=None):
        prod = Product.objects.get(pk=pk)
        return Response({'product': prod.product})
