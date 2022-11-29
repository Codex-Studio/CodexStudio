from django.contrib import admin
from apps.settings.models import Setting, ProjectType, Portfolio, Partners, Service, AboutUs, Benefits, Review, News, Contact, AboutUSImages

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "email", "phone"]

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "created"]
    
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "project_type", "url"]

class PartnersAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "url"]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "icon", "price"]

class AboutImageAdmin(admin.TabularInline):
    model = AboutUSImages
    extra = 1

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]
    inlines = [AboutImageAdmin]

class BenefitsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "icon"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name_surname', "job_title", "title", "created"]

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', "description", "created"]

admin.site.register(Setting, SettingAdmin)
admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Benefits, BenefitsAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(AboutUSImages)