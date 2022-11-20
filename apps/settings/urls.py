from django.urls import path 
from apps.settings.views import index, portfolio_index, portfolio_detail, services_index, contact

urlpatterns = [
    path('', index, name = "index"),
    path('portfolio/', portfolio_index, name = "portfolio_index"),
    path('portfolio/<int:id>/', portfolio_detail, name = "portfolio_detail"),
    path('services/', services_index, name = "services_index"),
    path('contact/', contact, name = "contact")
]