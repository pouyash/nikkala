from django.contrib import admin

# Register your models here.
from django.contrib.admin import register
from product.models import Product, Category, Brand


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'is_active']
    prepopulated_fields = {
        'slug': ('title',)
    }

@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'is_active']
    prepopulated_fields = {
        'slug': ('title',)
    }

@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'title']

    prepopulated_fields = {
        'slug': ('title',)
    }


