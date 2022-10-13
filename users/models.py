from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self,id,email,username,first_name,last_name,mobile_number,business_name,password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            id = id,
            username = username,
            first_name=first_name,
            last_name=last_name,
            mobile_number = mobile_number,
            business_name = business_name
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser= True
        user.is_staff= True
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,id,email,username,first_name,last_name,mobile_number,business_name,password=None):
        user = self.create_user(
            id,
            email,
            username,
            first_name,
            last_name,
            mobile_number,
            business_name,
            password=password,

        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser= True
        user.is_staff= True
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin):
    
    username=models.CharField(max_length=255,null=True,blank=True,unique=True)
    first_name=models.CharField(max_length=255,null=False,blank=False)
    last_name=models.CharField(max_length=255,null=False,blank=False)
    email=models.EmailField(max_length=255,unique=True)
    mobile_number=models.CharField(max_length=255,null=False,blank=False)
    is_mobile_veriefied = models.BooleanField(default=False)
    business_name=models.CharField(max_length=255,null=False,blank=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    objects = UserAccountManager()

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["id","username","first_name","last_name","mobile_number","business_name"]


    class Meta:
        verbose_name_plural = "Users"




    def __str__(self):
        return self.email
