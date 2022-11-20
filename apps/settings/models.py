from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип проекта"
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank = True, null = True
    )
    phone = models.CharField(
        max_length=200,
        verbose_name="Номер телефона"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"