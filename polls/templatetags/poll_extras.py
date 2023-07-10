from django import template

register = template.Library()

@register.filter
def three_digit(val):
    return "{:,}".format(val)