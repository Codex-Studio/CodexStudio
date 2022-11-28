# Generated by Django 4.1.3 on 2022-11-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0014_setting_url_maps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='url_maps',
            field=models.URLField(blank=True, default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1516.504442753528!2d72.80188400298358!3d40.519294688957466!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38bdaf43b0b9c00f%3A0x1aa9c672c00b1a9e!2z0JLQndCX0JjQntCd!5e0!3m2!1sru!2skg!4v1669628615604!5m2!1sru!2skg', max_length=500, null=True, verbose_name='URL адрес Google Карты'),
        ),
    ]
