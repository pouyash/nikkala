from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from user.models import User


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_active', 'is_superuser']