from datetime import datetime

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


@register.filter
def get_date(value):
    now = datetime.now().astimezone(value.tzinfo)
    time_difference = now - value

    days = time_difference.days

    hours = time_difference.seconds // 3600
    # minutes = (time_difference.seconds // 60) % 60

    if days > 0:
        time_str = f"{days} روز "
    else:
        time_str = ""

    if hours > 0:
        if time_str:
            time_str += "و "
        time_str += f"{hours} ساعت"


    # if minutes > 0:
    #     if time_str:
    #         time_str += " و "
    #     time_str += f"{minutes} دقیقه "


    return time_str + " قبل"
