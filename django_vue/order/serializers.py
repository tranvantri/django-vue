from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'price',
            'book',
            'quantity',
        )


class OrderSerializer(serializers.ModelSerializer):
    book_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'zipcode',
            'place',
            'phone',
            'created_at',
            'stripe_token',
            'paid_amount',
            'book_items'
        )

    def create(self, validated_data):
        items_data = validated_data.pop('book_items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
