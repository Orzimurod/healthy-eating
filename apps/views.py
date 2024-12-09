from django.shortcuts import render
from .models import About, Blog, Service

def home(request):
    return render(request, 'index.html')


def about_view(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about})


def service_view(request):
    service = Service.objects.all()[:3]
    return render(request, 'service.html', {'service': service})


def blog_view(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog})


from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')
