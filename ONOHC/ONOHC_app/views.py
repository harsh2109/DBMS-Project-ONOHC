from django.shortcuts import render
from django.http import HttpResponse
from ONOHC_app.models import Signin

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def signin(request):
    if request.method == "GET":
        email = request.GET.get('email')
        username = request.GET.get('username')
        password = request.GET.get('password')
        city = request.GET.get('city')
        state = request.GET.get('state')
        Zip = request.GET.get('Zip')
        signin= Signin(email= email, username= username, password = password, city= city, state=state, Zip=Zip)
        signin.save()
    return render(request, 'signin.html')

    
