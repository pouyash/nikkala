# Generated by Django 4.2 on 2023-07-31 16:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_commentblog_dislike_count_commentblog_like_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentblog',
            name='user_reaction',
            field=models.ManyToManyField(blank=True, related_name='blog_comment_like', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
