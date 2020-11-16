from django.urls import path
from . import views

urlpatterns = [
    path('index.html/', views.home, name='Homepage'),
    path('about.html/', views.about, name= 'AboutUs'),
    path('login.html/', views.login, name= 'Login'),
    path('signin.html/', views.signin, name= 'Signin'),
]