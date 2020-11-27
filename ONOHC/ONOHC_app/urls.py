from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Homepage'),
    path('index/', views.home, name='Homepage'),
    path('about/', views.about, name= 'AboutUs'),
    path('login/', views.login, name= 'Login'),
    path('signin/', views.signin, name= 'Signin'),
]