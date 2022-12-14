# Generated by Django 4.1.3 on 2022-11-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_projecttype_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Цена проекта'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(default=1, verbose_name='Ссылка на проект'),
            preserve_default=False,
        ),
    ]
