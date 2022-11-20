from django.contrib import admin
from apps.settings.models import Setting, ProjectType, Portfolio, Partners, Service

# Register your models here.
admin.site.register(Setting)
admin.site.register(ProjectType)
admin.site.register(Portfolio)
admin.site.register(Partners)
admin.site.register(Service)