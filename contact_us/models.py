from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان')
    fullname = models.CharField(max_length=700, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=15, verbose_name='تلفن',validators=[MaxLengthValidator(11), MinLengthValidator(11)])
    message = models.TextField(verbose_name='متن پیغام')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname + " " + self.title

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'

