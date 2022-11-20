# Generated by Django 4.1.3 on 2022-11-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя услуги')),
                ('icon', models.ImageField(upload_to='service_icon/', verbose_name='Иконка услуги')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]