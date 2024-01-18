from rest_framework import serializers

from .models import Order


class AllOrdersSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class AddOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ViewOrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class EditOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class DeleteOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
