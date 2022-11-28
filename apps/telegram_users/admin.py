from django.contrib import admin
from apps.telegram_users.models import TelegramUser

# Register your models here.
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'chat_id', 'username', 'first_name', 'last_name', 'added']
    readonly_fields = ['user_id', 'chat_id', 'username', 'first_name', 'last_name', 'added', 'ip_address']

admin.site.register(TelegramUser, TelegramUserAdmin)