from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=300, default='درباره ما', verbose_name='درباره ما')
    context = RichTextUploadingField(verbose_name='متن')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + str(self.is_active) + str(self.created_at)

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
