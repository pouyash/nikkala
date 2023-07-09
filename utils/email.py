from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template.defaultfilters import striptags
from django.template.loader import render_to_string


def send_email(subject, to, context, template):
    try:
        message = render_to_string(template, context)
        messages = striptags(message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, messages, from_email, recipient_list=[to])
    except:
        raise ValidationError('مشکل در اسال ایمیل لطفا مجددا تلاش نمائید')
