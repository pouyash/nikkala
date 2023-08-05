from django import template
from jalali_date import datetime2jalali

register = template.Library()

@register.filter
def three_digit(val):
    return "{:,}".format(val)

@register.filter
def jalali_date(val):
    return datetime2jalali(val).strftime("%Y/%m/%d")

@register.filter
def jalali_time(val):
    return datetime2jalali(val).strftime("%H:%M")

@register.filter
def jalali_date_time(val):
    return datetime2jalali(val).strftime("%Y/%m/%d | %H:%M")

@register.filter
def has_favorite(product, user):
    return product.user_like.filter(id=user.id).exists()