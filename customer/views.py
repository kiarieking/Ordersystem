from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'customer/base.html')


def registration_form(request):
    return render(request, 'customer/register.html')


def register(request):
    fname = request.POST.get('firstname')
    lname = request.POST.get('lastname')
    contactno = request.POST.get('contactnumber')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.method == 'POST':
        User.objects.create_user(username=fname, first_name=fname, last_name=lname, email=email, password=password)
        #Account created successfully alert

    return redirect(home)


def login_form(request):
    return render(request, 'customer/login.html')

