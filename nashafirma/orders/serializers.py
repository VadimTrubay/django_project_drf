from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Order, OrderItem


class MetaOrder:
    class Meta:
        model = Order
        fields = '__all__'

class MetaOrderItem:
    class Meta:
        model = OrderItem
        fields = '__all__'


class AllOrdersReadSerializer(serializers.ModelSerializer, MetaOrder):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    products = serializers.SlugRelatedField(slug_field="product", read_only=True, many=True)


class AllOrdersWriteSerializer(serializers.ModelSerializer, MetaOrder):
    pass

class OrderReadSerializer(serializers.ModelSerializer, MetaOrder):
    # user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    products = serializers.SlugRelatedField(slug_field="product", read_only=True, many=True)
    # pass


class OrderWriteSerializer(serializers.ModelSerializer, MetaOrder):
    pass

class AllItemsReadSerializer(serializers.ModelSerializer, MetaOrderItem):
    product = serializers.SlugRelatedField(slug_field="product", read_only=True)

class AllItemsWriteSerializer(serializers.ModelSerializer, MetaOrderItem):
    pass

class ItemsReadSerializer(serializers.ModelSerializer, MetaOrderItem):
    order = serializers.SlugRelatedField(slug_field="created_at", read_only=True)
    product = serializers.SlugRelatedField(slug_field="product", read_only=True)
    # pass

class ItemsWriteSerializer(serializers.ModelSerializer, MetaOrderItem):
    pass
