from django.urls import path
from apps.views import about_view, blog_view, home, service_view

urlpatterns = [
    path('', home, name='home'),
    path('about', about_view, name='about'),
    path('service', service_view, name='service'),
    path('blog', blog_view, name='blog'),
]
