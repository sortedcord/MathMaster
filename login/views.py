from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if password_repeat != password:
            messages.info(request, 'Passwords Do not Match')
            return redirect('/account/register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken. Please chose a new username')
            return redirect('/account/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'This email has already been used by another account. Please Login.')
            return redirect('/account/register')
        else:
            user = User.objects.create_user(username=username, password=password_repeat, email=email,
                                            first_name=first_name, last_name=last_name)
            user.save()
            print("Created User")
            return redirect('/account/login')

    else:
        html = render(request, "register.html")
        return HttpResponse(html)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            return redirect("/index.html")
        else:
            messages.info(request, 'The Email or The Password is incorrect')
            return redirect("/account/login")
    else:
        html = render(request, "login.html")
        return HttpResponse(html)
