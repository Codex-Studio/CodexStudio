from django.urls import path 
from apps.settings.views import index, portfolio_index, portfolio_detail, services_index, contact, about_us, news_index, news_detail, error

urlpatterns = [
    path('', index, name = "index"),
    path('portfolio/', portfolio_index, name = "portfolio_index"),
    path('portfolio/<int:id>/', portfolio_detail, name = "portfolio_detail"),
    path('services/', services_index, name = "services_index"),
    path('contact/', contact, name = "contact"),
    path('about_us/', about_us, name = "about_us"),
    path('news/', news_index, name = "news_index"),
    path('news/<int:id>/', news_detail, name="news_detail"),
    path('404/', error, name="error")
]