from django.contrib import admin

from .models import Currency, Order, OrderType, OrderVariety


@admin.register(OrderType)
class OrderTypeAdmin(admin.ModelAdmin):
    list_display = [
        "type",
    ]


@admin.register(OrderVariety)
class OrderVarietyAdmin(admin.ModelAdmin):
    list_display = [
        "variety",
    ]


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_type",
        "order_variety",
        "currency",
        "tiker",
        "count",
        "type",
        "number",
        "date",
        "duration",
    ]
