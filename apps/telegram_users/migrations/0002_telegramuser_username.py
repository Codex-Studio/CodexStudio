# Generated by Django 4.1.3 on 2022-11-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(default='Toktorov2', max_length=255, verbose_name='Имя пользователя телеграм'),
        ),
    ]
