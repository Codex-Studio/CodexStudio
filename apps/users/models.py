from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id_telegram = models.PositiveBigIntegerField(
        verbose_name="id телеграмм аккаунта для админки",
        null = True, blank = True
    )

    def __str__(self):
        return f"{self.id_telegram}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"