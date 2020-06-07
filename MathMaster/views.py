from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    html = render(request, "index.html")
    return HttpResponse(html)
