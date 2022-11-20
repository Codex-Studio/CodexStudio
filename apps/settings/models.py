from django.db import models
from django_resized.forms import ResizedImageField

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


class ProjectType(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Тип проекта"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Тип проекта"
        verbose_name_plural = "Тип проектов"

class Portfolio(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название проекта"
    )
    description = models.TextField(
        verbose_name="Описание проекта"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='project_images/',
        verbose_name="Фотография проекта")
    project_type = models.ForeignKey(
        ProjectType,
        on_delete=models.SET_NULL,
        related_name="portfolio_project_type",
        verbose_name="Тип проекта",
        null = True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолии"