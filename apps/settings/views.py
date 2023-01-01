from django.shortcuts import render, redirect
from apps.settings.models import Setting, Portfolio, Partners, Service, AboutUs, ProjectType, Benefits, Review, News, Contact

# Create your views here.
def index(request):
    try:
        setting = Setting.objects.latest('id')
        about = AboutUs.objects.latest('id')
    except:
        return render(request, 'page_404.html')
    partners = Partners.objects.all().order_by('-id')
    services = Service.objects.all().order_by('?')[:3]
    project_type = ProjectType.objects.all()
    portfolio = Portfolio.objects.all()
    benefits = Benefits.objects.all().order_by('?')
    reviews = Review.objects.all().order_by('?')
    news = News.objects.all().order_by('created')
    context = {
        'setting' : setting,
        'partners' : partners,
        'services' : services,
        'about' : about,
        'project_type' : project_type,
        'portfolio' : portfolio,
        'benefits' : benefits,
        'reviews' : reviews,
        'news' : news,
    }
    return render(request, 'index.html', context)

def portfolio_index(request):
    setting = Setting.objects.latest('id')
    portfolio = Portfolio.objects.all().order_by('-id')
    services = Service.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'portfolio' : portfolio,
        'services' : services,
    }
    return render(request, 'portfolio.html', context)

def portfolio_detail(request, id):
    setting = Setting.objects.latest('id')
    portfolio = Portfolio.objects.get(id = id)
    about = AboutUs.objects.latest('id')
    random_portfolio = Portfolio.objects.all().order_by('?')
    services = Service.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'portfolio' : portfolio,
        'about' : about,
        'random_portfolio' : random_portfolio,
        'services' : services,
    }
    return render(request, 'portfolio_detail.html', context)

def services_index(request):
    setting = Setting.objects.latest('id')
    services = Service.objects.all().order_by('-id')
    reviews = Review.objects.all().order_by('?')
    context = {
        'setting' : setting,
        'services' : services,
        'reviews' : reviews,
    }
    return render(request, 'services.html', context)

def contact(request):
    setting = Setting.objects.latest('id')
    services = Service.objects.all().order_by('-id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact = Contact.objects.create(name = name, email = email, phone = phone, subject = subject)
        return redirect('index')
    context = {
        'setting' : setting,
        'services': services,
    }
    return render(request, 'contact.html', context)

def about_us(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    portfolio = Portfolio.objects.all()
    partners = Partners.objects.all().order_by('-id')
    first_news = News.objects.all().order_by('-created')[:1]
    news = News.objects.all().order_by('-created')[1:]
    services = Service.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'about' : about,
        'portfolio' : portfolio,
        'partners' : partners,
        'first_news' : first_news,
        'news' : news,
        'services' : services,
    }
    return render(request, 'about.html', context)

def news_index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all().order_by('created')
    random_news = News.objects.all().order_by('?')[:1]
    services = Service.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'news' : news,
        'random_news' : random_news,
        'services' : services,
    }
    return render(request, 'news.html', context)

def news_detail(request, id):
    setting = Setting.objects.latest('id')
    news = News.objects.get(id = id)
    services = Service.objects.all().order_by('-id')
    context = {
        'setting' : setting,
        'news' : news,
        'services' : services,
    }
    return render(request, 'news_detail.html', context)

def error(request):
    return render(request, 'page_404.html')

def handler404(request, exception):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    response = render(request, "page_404.html", context)
    response.status_code = 404
    return response