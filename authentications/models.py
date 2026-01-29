from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('The email field must be send')
        
        email=self.normalize_email(email=email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if not extra_fields.get('is_staff'):
            raise ValueError('Super_user must have is_staff=True')
        
        if not extra_fields.get('is_superuser'):
            raise ValueError('Super_user must have is_superuser=True')
        return self.create_user(email=email,password=password,**extra_fields)



class CustomUsers(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    address=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=15,unique=True,blank=True,null=True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):
        return self.email