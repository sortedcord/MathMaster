from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    html = render(request, "register.html")
    return HttpResponse(html)


def login(request):
    html = render(request, "login.html")
    return HttpResponse(html)
