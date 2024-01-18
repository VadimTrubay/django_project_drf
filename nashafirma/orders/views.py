from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .serializers import *


class AllOrdersViewSet(generics.ListAPIView):
    queryset = Order.objects.all()

    # serializer_class = AllOrdersSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllOrdersReadSerializer
        elif self.request.method == 'PUT' or self.request.method == 'PATH':
            return AllOrdersWriteSerializer
        return AllOrdersReadSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    # serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderReadSerializer
        elif self.request.method == 'PUT' or self.request.method == 'PATH':
            return OrderWriteSerializer
        return OrderReadSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Order.objects.all()
        return Order.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def order(self, request, pk=None):
        ordr = Order.objects.get(pk=pk)
        return Response({'order': ordr.created_at})


class AllItemsViewSet(generics.ListAPIView):
    queryset = OrderItem.objects.all()

    # serializer_class = AllItemsSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllItemsReadSerializer
        elif self.request.method == 'PUT' or self.request.method == 'PATH':
            return AllItemsWriteSerializer
        return AllItemsReadSerializer


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()

    # serializer_class = ItemsSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ItemsReadSerializer
        elif self.request.method == 'PUT' or self.request.method == 'PATH':
            return ItemsWriteSerializer
        return ItemsReadSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return OrderItem.objects.all()
        return OrderItem.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def order_item(self, request, pk=None):
        ordr_itm = OrderItem.objects.get(pk=pk)
        calc = OrderItem.calculate_total(ordr_itm)
        return Response({'order_item': ordr_itm.product, 'total': calc})
