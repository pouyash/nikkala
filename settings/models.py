from django.core.validators import FileExtensionValidator
from django.db import models


class Slider(models.Model):
    image = models.ImageField(upload_to='slider', verbose_name='تصویر')
    alt = models.CharField(max_length=400, verbose_name='توضیحات تصویر', null=True, blank=True)
    link = models.TextField(verbose_name='آدرس ریدایرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر'


class AdvertiseTopIndex(models.Model):
    image = models.ImageField(upload_to='advertise/top', verbose_name='تصویر')
    alt = models.CharField(max_length=400, verbose_name='توضیحات تصویر', null=True, blank=True)
    link = models.TextField(verbose_name='آدرس ریدایرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'تبلیغ صفحه اصلی - قسمت بالایی'
        verbose_name_plural = 'تبلیغ صفحه اصلی - قسمت بالایی'



class AdvertiseMiddleIndex(models.Model):
    image = models.ImageField(upload_to='advertise/middle', verbose_name='تصویر')
    alt = models.CharField(max_length=400, verbose_name='توضیحات تصویر', null=True, blank=True)
    link = models.TextField(verbose_name='آدرس ریدایرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'تبلیغ صفحه اصلی - قسمت وسطی'
        verbose_name_plural = 'تبلیغ صفحه اصلی - قسمت وسطی'


class AdvertiseBottomIndex(models.Model):
    image = models.ImageField(upload_to='advertise/bottom', verbose_name='تصویر')
    alt = models.CharField(max_length=400, verbose_name='توضیحات تصویر', null=True, blank=True)
    link = models.TextField(verbose_name='آدرس ریدایرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'تبلیغ صفحه اصلی - قسمت پایینی'
        verbose_name_plural = 'تبلیغ صفحه اصلی - قسمت پایینی'



class FooterCapability(models.Model):
    title = models.CharField(max_length=600, verbose_name='عنوان')
    image = models.FileField(upload_to='footer/capability/%y/%m/', validators=[FileExtensionValidator(['jpg', 'svg', 'jpeg', 'png'])])
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'توانمندی ها - فوتر'
        verbose_name_plural = 'توانمندی ها - فوتر'
