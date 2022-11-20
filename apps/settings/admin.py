from django.contrib import admin
from apps.settings.models import Setting, ProjectType, Portfolio

# Register your models here.
admin.site.register(Setting)
admin.site.register(ProjectType)
admin.site.register(Portfolio)