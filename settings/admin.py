from django.contrib import admin
from django.contrib.admin import register

from settings.models import Slider, AdvertiseTopIndex, AdvertiseMiddleIndex, AdvertiseBottomIndex, FooterCapability, \
    Footer, FooterImages, SocialMedia


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


@register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    list_editable = ('is_active',)


@register(FooterImages)
class FooterImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'footer', 'is_active']
    list_editable = ('is_active',)


@register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'link', 'is_active']
    list_editable = ('is_active', 'link', 'title',)

