# myapp/interfaces/api/serializers.py
from rest_framework import serializers
from onboarding.domain.aggregate import OrderLine


class OrderLineSerializer(serializers.Serializer):
    product = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)


class CustomerSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()


class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    customer = CustomerSerializer()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    order_lines = OrderLineSerializer(many=True)
