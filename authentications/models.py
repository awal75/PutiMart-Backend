from django.db import models
from django.contrib.auth.models import AbstractUser

class

class CustomUsers(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    address=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=15,unique=True,blank=True,null=True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

