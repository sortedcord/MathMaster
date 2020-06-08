from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html = render(request, "index.html")
    return HttpResponse(html)


def image_of_the_day(request):
    html = render(request, "image-of-the-day.html")
    return HttpResponse(html)


def profile(request):
    html = render(request, "profile.html")
    return HttpResponse(html)


def table(request):
    html = render(request, "table.html")
    return HttpResponse(html)


def register(request):
    html = render(request, "register.html")
    return HttpResponse(html)


def login(request):
    html = render(request, "login.html")
    return HttpResponse(html)


def announcements(request):
    html = render(request, "announcements.html")
    return HttpResponse(html)
