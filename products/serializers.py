from rest_framework import serializers
from .models import Product, Order, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "product",
            "quantity",
            "total_price",
            "is_paid",
            "created_at",
        ]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "price", "cart"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "created_at"]
