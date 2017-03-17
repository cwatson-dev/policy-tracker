from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)
    inPower = models.CharField(max_length=64)
    slug = models.SlugField()

class Promise(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    category = models.CharField(mac_length=64)

class Category(models.Model):
    

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
