from django.db import models
from django.contrib.auth.models import User
import json
import urllib.request as request

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Parent_Childs(models.Model):
    Parent_Username= models.CharField(max_length=50)
    Child_Username=models.CharField(max_length=50)

class Parkimg(models.Model):

    park = models.OneToOneField('B7data', on_delete=models.CASCADE)
    image = models.ImageField(default='default2.jpg', upload_to='park_pics')



class B7data(models.Model):
    Name = models.CharField(max_length=40, blank=True, null=True)
    surface = models.CharField(max_length=40, blank=True, null=True)
    shadowing = models.CharField(max_length=10, blank=True, null=True)
    combined1 = models.IntegerField(default=0)
    combined2 = models.IntegerField(default=0)
    combined3 = models.IntegerField(default=0)
    SpecialCom = models.IntegerField(default=0)
    Swing = models.IntegerField(default=0)
    slid = models.IntegerField(default=0)
    carrousel = models.IntegerField(default=0)
    spring = models.IntegerField(default=0)
    omega = models.IntegerField(default=0)
    roserose = models.IntegerField(default=0)
    other = models.CharField(max_length=40, blank=True, null=True)
    lat = models.FloatField(default=0.00)
    lon = models.FloatField(default=0.00)


class Location():
    def __init__(self,a,l):
        self.lat=a
        self.lon =l


