from django.contrib import admin
from django.contrib.admin import register

from settings.models import Slider, AdvertiseTopIndex, AdvertiseMiddleIndex, AdvertiseBottomIndex, FooterCapability


@register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'is_active', 'alt']
    list_editable = ('is_active',)


@register(AdvertiseTopIndex)
class AdvertiseTopIndexAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'is_active', 'alt']
    list_editable = ('is_active',)


@register(AdvertiseMiddleIndex)
class AdvertiseMiddleIndexAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'is_active', 'alt']
    list_editable = ('is_active',)


@register(AdvertiseBottomIndex)
class AdvertiseBottomIndexAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'is_active', 'alt']
    list_editable = ('is_active',)



@register(FooterCapability)
class FooterCapabilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'is_active']
    list_editable = ('is_active',)