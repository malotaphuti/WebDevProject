from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as auth_login
from django.conf import settings
from django.shortcuts import redirect
from django.views import View

def home(request):
    return render(request, 'home.html')

# Create your views here.
from django.shortcuts import render

def register(request):
    # Your registration logic here
    return render(request, 'register.html')

def login(request):
    # Your registration logic here
    return render(request, 'login.html')
