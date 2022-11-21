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
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank = True, null = True
    )
    telegram_bot = models.URLField(
        max_length=255,
        verbose_name="Ссылка на бот",
        blank = True, null = True
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
    url = models.URLField(
        verbose_name="Ссылка на проект"
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена проекта",
        default=0,
        blank = True, null = True
    )
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

class Partners(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название партнеров"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='project_images/',
        verbose_name="Фотография проекта"
    )
    url = models.URLField(
        verbose_name="Ссылка на парнера"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Имя услуги"
    )
    icon = models.ImageField(
        upload_to="service_icon/",
        verbose_name="Иконка услуги"
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена услуги"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class AboutUs(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='project_images/',
        verbose_name="Фотография проекта"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Benefits(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название преимущества"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание преимущества"
    )
    icon = models.ImageField(
        upload_to="benefits_icons",
        max_length=255,
        verbose_name="Иконка преимущества"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

class Review(models.Model):
    name_surname = models.CharField(
        max_length=255,
        verbose_name="Имя и фамилия"
    )
    job_title = models.CharField(
        max_length=100,
        verbose_name="Должность"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='review_images/',
        verbose_name="Фотография клиента"
    )
    title = models.TextField(
        verbose_name="Отзыв"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='news_images/',
        verbose_name="Фотография"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"