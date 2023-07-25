from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from user.models import User


class CategoryBlog(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان')
    parent = models.ForeignKey('CategoryBlog', null=True, blank=True, verbose_name='دسته بندی والد', on_delete=models.CASCADE, related_name='category_parent')
    slug = models.SlugField(allow_unicode=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیررفعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'دسته بندی وبلاگ'
        verbose_name_plural = 'دسته بندی های وبلاگ'

    def __str__(self):
        return self.slug


class Tag(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان')
    slug = models.SlugField(allow_unicode=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیررفعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'هشتگ'
        verbose_name_plural = 'هشتگ ها'

    def __str__(self):
        return self.slug


class Blog(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog', auto_created=True, verbose_name='نویسنده')
    slug = models.SlugField(allow_unicode=True, verbose_name='عنوان در url')
    category = models.ForeignKey(CategoryBlog, related_name='blog', verbose_name='دسته بندی', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='blog', verbose_name='هشتگ ها')
    image = models.ImageField(upload_to='blog', verbose_name='تصویر')
    short_description = models.TextField(verbose_name='توضیحات مختصر')
    description = RichTextUploadingField(null=True, blank=True, verbose_name='توضیحات')

    is_active = models.BooleanField(default=True, verbose_name='فعال / غیررفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug + " " + str(self.user)

    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = "وبلاگ"


class CommentBlog(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    parent = models.ForeignKey("CommentBlog", null=True, blank=True, related_name='comment_blog_parent', on_delete=models.CASCADE, verbose_name='ادمین-پاسخ')
    comment = models.TextField(verbose_name='متن کامنت')
    blog = models.ForeignKey(Blog, related_name='comment_blog', on_delete=models.CASCADE, verbose_name='مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
