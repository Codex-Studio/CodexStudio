from django.shortcuts import render
from apps.settings.models import Setting, Portfolio, Partners, Service

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    partners = Partners.objects.all().order_by('-id')
    services = Service.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'partners' : partners,
        'services' : services,
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

def portfolio_detail(request, id):
    setting = Setting.objects.latest('id')
    portfolio = Portfolio.objects.get(id = id)
    context = {
        'setting' : setting,
        'portfolio' : portfolio,
    }
    return render(request, 'portfolio_detail.html', context)

def services_index(request):
    setting = Setting.objects.latest('id')
    services = Service.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'services' : services,
    }
    return render(request, 'services.html', context)

def contact(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request, 'contact.html', context)