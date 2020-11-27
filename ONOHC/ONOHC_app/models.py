from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signin(models.Model):
    email= models.CharField(max_length=30,null=True)
    username= models.CharField(max_length=30,null=True)
    password= models.CharField(max_length=20,null=True)
    city= models.CharField(max_length=20,null=True)
    state= models.CharField(max_length=20,null=True)
    Zip= models.CharField(max_length=20,null=True)