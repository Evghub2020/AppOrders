from rest_framework import serializers

from ..models import Currency, Order, OrderType, OrderVariety


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = "__all__"


class OrderVarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderVariety
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_type = OrderTypeSerializer()
    order_variety = OrderVarietySerializer()
    currency = CurrencySerializer()

    class Meta:
        model = Order
        fields = "__all__"
