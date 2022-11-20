from django.shortcuts import render
from apps.settings.models import Setting, Portfolio

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'index.html', context)

def about_us(request):
    return render()

def portfolio_index(request):
    setting = Setting.objects.latest('id')
    portfolio = Portfolio.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'portfolio' : portfolio,
    }
    return render(request, 'portfolio.html', context)