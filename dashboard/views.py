from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from dashboard.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    html = render(request, "index.html",)
    return HttpResponse(html)


@login_required
def image_of_the_day(request):
    html = render(request, "image-of-the-day.html",)
    return HttpResponse(html)

@login_required
def profile(request):
    html = render(request, "profile.html", )
    return HttpResponse(html)

@login_required
def play(request):
    html = render(request, "play.html", )
    return HttpResponse(html)


def login(request):
    html = render(request, "login.html",)
    return HttpResponse(html)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

