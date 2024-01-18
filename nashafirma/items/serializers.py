from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Item
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Order
        fields = ['created_at', 'user', 'done']


class AllItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = serializers.SlugRelatedField(slug_field="product", read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class AddItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ViewItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = serializers.SlugRelatedField(slug_field="product", read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class EditItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class DeleteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
