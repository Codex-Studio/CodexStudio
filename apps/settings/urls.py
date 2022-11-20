from django.urls import path 
from apps.settings.views import index, portfolio_index

urlpatterns = [
    path('', index, name = "index"),
    path('portfolio/', portfolio_index, name = "portfolio_index"),
]