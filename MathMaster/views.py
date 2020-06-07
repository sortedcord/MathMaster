from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html = render(request, "index.html")
    return HttpResponse(html)
