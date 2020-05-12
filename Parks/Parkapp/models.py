from django.db import models
from django.contrib.auth.models import User
import json
import urllib.request as request

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Parkimg(models.Model):

    park = models.OneToOneField('B7data', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='park_pics')



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



    # def __init__(self,i):
    #     super(B7data, self).__init__()
    #     self.Name = i['Name']
    #     self.surface = i['surface']
    #     self.shadowing = i['shadowing']
    #     self.combined1 = i['combined1']
    #     self.combined2 = i['combined2']
    #     self.combined3 = i['combined3']
    #     self.SpecialCom = i['SpecialCom']
    #     self.Swing = i['Swing']
    #     self.slid = i['slid']
    #     self.carrousel = i['carrousel']
    #     self.spring = i['spring']
    #     self.omega = i['omega']
    #     self.roserose = i['roserose']
    #     self.other = i['other']
    #     self.lat = i['lat']
    #     self.lon = i['lon']



