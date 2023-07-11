from django.contrib import admin
# Register your models here.
from django.contrib.admin import register

from about_us.models import AboutUs


@register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'title']
