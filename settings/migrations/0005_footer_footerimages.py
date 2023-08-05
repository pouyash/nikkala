# Generated by Django 4.2 on 2023-08-04 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_alter_footercapability_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('verify', models.TextField(verbose_name='اعتبار')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'بخش فوتر',
                'verbose_name_plural': 'بخش فوتر',
            },
        ),
        migrations.CreateModel(
            name='FooterImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='footer/%y/%m/', verbose_name='تصویر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیرفعال')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_images', to='settings.footer', verbose_name='فوتر')),
            ],
            options={
                'verbose_name': 'تصویر فوتر',
                'verbose_name_plural': 'تصویر فوتر',
            },
        ),
    ]