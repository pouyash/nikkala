from django.contrib import admin
from django.contrib.admin import register

from order.models import Order, OrderDetail


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_paid', 'user']


@register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'count']
