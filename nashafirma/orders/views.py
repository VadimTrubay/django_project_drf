from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import *


class GetPermissionsMixin:
    def get_permissions(self):
        if str(self.request.user) == 'admin':
            self.queryset = Order.objects.all()
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
            self.queryset = Order.objects.filter(user=self.request.user)
        return super().get_permissions()


class AllOrdersViewSet(GetPermissionsMixin, generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = AllOrdersSerializer


class AddOrderViewSet(GetPermissionsMixin, generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AddOrderSerializer


class ViewOrderViewSet(GetPermissionsMixin, generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = ViewOrderSerializer


class EditOrderViewSet(GetPermissionsMixin, generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = EditOrderSerializer


class DeleteOrderViewSet(GetPermissionsMixin, generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = DeleteOrderSerializer
