from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html = render(request, "index.html", {'name': "John Doe"})
    return HttpResponse(html)


def image_of_the_day(request):
    html = render(request, "image-of-the-day.html", {'name': "John Doe"})
    return HttpResponse(html)


def profile(request):
    html = render(request, "profile.html", {'name': "John Doe"})
    return HttpResponse(html)


def table(request):
    html = render(request, "table.html", {'name': "John Doe"})
    return HttpResponse(html)


def announcements(request):
    html = render(request, "announcements.html", {'name': "John Doe"})
    return HttpResponse(html)
