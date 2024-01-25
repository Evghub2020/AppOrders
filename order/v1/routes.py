from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrencyViewSet, OrderTypeViewSet, OrderVarietyViewSet, OrderViewSet

app_name = "order"

router = DefaultRouter()
router.register(r"currency", CurrencyViewSet, basename="currency")
router.register(r"order_type", OrderTypeViewSet, basename="order_type")
router.register(r"order_variety", OrderVarietyViewSet, basename="order_variety")

router.register(r"order", OrderViewSet, basename="order")

urlpatterns = router.urls
