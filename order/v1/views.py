from rest_framework import viewsets

from ..models import Currency, Order, OrderType, OrderVariety
from .serializers import (
    CurrencySerializer,
    OrderSerializer,
    OrderTypeSerializer,
    OrderVarietySerializer,
)


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class OrderTypeViewSet(viewsets.ModelViewSet):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer


class OrderVarietyViewSet(viewsets.ModelViewSet):
    queryset = OrderVariety.objects.all()
    serializer_class = OrderVarietySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
