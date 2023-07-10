from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.core.files.storage import DefaultStorage
from django.db import models
from django.utils.text import slugify
from filebrowser.fields import FileBrowseField

# file = FileBrowseField("File", max_length=200)


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='دسته بندی')
    parent = models.ForeignKey('Category', related_name='category', null=True, blank=True, on_delete=models.CASCADE, verbose_name='دسته بندی والد')
    slug = models.SlugField(max_length=400, verbose_name='عنوان در url', allow_unicode=True, unique=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     self.slug = slugify(self.title)
    #     super(Category, self).save()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Brand(models.Model):
    title = models.CharField(max_length=300, verbose_name='برند')
    slug = models.SlugField(max_length=400, verbose_name='عنوان در url', allow_unicode=True, unique=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     self.slug = slugify(self.title)
    #     super(Brand, self).save()

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برندها'

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    slug = models.SlugField(max_length=400, verbose_name='عنوان در url', allow_unicode=True, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product', verbose_name='برند')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', verbose_name='دسته بندی')
    image = models.ImageField(upload_to='product', verbose_name='تصویر')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    short_description = models.TextField(null=True, blank=True, verbose_name='توضحیات مختصر')
    description = RichTextUploadingField(null=True, blank=True, verbose_name='توضیحات')
    number = models.PositiveIntegerField(verbose_name='تعداد')

    guarantee = models.CharField(max_length=100, verbose_name='گارانتی')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.slug

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Product, self).save()

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'