# Generated by Django 4.1.3 on 2022-11-22 05:37

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUSImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='about_images/', verbose_name='Фотография проекта')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_us_images', to='settings.aboutus')),
            ],
            options={
                'verbose_name': 'О нас доп фото',
                'verbose_name_plural': 'О нас доп фото',
            },
        ),
    ]
