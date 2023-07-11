from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from contact_us.models import ContactUs


@register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'message']