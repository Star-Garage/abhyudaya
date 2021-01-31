from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    username=models.CharField(max_length=20, default="the_meetpatel")
    otp=models.IntegerField(default=456)
    mobile=models.CharField(max_length=15,)
    is_active=models.BooleanField(default=True)
    is_verfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)
    first_time_login=models.BooleanField(default=False)

class Provider(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    #update profile:
    name=models.CharField(max_length=30,blank=True)
    gender=models.CharField(max_length= 10,blank=True)
    country=models.CharField(max_length=50,blank=True)
    address=models.CharField(max_length=50,blank=True)
    state=models.CharField(max_length=15,blank=True)
    city=models.CharField(max_length=20,blank=True)
    pincode=models.CharField(max_length=6,blank=True)
    
class Customer(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    #update profile:
    name=models.CharField(max_length=30,blank=True)
    gender=models.CharField(max_length= 10,blank=True)
    country=models.CharField(max_length=50,blank=True)
    address=models.CharField(max_length=50,blank=True)
    state=models.CharField(max_length=15,blank=True)
    city=models.CharField(max_length=20,blank=True)
    pincode=models.CharField(max_length=6,blank=True)

class iInquiry(models.Model):
    i_fname=models.CharField(max_length=30,blank=True)
    i_lname=models.CharField(max_length=30,blank=True)
    i_email=models.EmailField(unique=True)
    i_contact=models.CharField(max_length=10,blank=True)
    i_msg=models.CharField(max_length=400,blank=True)