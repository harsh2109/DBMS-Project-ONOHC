from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'ONOHC_app/index.html')

def about(request):
    return render(request, 'ONOHC_app/about.html')

def login(request):
    return render(request, 'ONOHC_app/login.html')

def signin(request):
    return render(request, 'ONOHC_app/signin.html')

    
