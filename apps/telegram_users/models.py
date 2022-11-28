from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    user_id = models.BigIntegerField(
        verbose_name="id телеграм пользователя",
    )
    chat_id = models.BigIntegerField(
        verbose_name="chat id"
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        blank = True, null = True,
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank = True, null = True,
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя телеграм",
        default="Toktorov2"
    )
    ip_address = models.CharField(
        max_length=255,
        verbose_name="IP адрес пользователя",
        blank = True, null = True,
    )
    added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Добавлен"
    )

    def __str__(self):
        return str(self.user_id)

    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"