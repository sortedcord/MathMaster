"""MathMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MathMaster import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/index.html', views.index),
    path('home/image-of-the-day.html', views.image_of_the_day),
    path('home/profile.html', views.profile),
    path('home/register.html', views.register),
    path('home/login.html', views.login),
    path('home/table.html', views.table),
    path('home/announcements.html', views.announcements),
]
