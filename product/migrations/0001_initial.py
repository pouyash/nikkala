# Generated by Django 4.2 on 2023-07-04 17:40

from django.db import migrations, models
import django.db.models.deletion
import filebrowser.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='برند')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='دسته بندی')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='برند')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, unique=True, verbose_name='عنوان در url')),
                ('image', filebrowser.fields.FileBrowseField(max_length=400, verbose_name='بارگذاری تصویر')),
                ('price', models.BigIntegerField()),
                ('number', models.IntegerField(verbose_name='تعداد')),
                ('garanty', models.CharField(max_length=100, verbose_name='گارانتی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.brand', verbose_name='برند')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.category', verbose_name='دسته بندی')),
            ],
        ),
    ]
