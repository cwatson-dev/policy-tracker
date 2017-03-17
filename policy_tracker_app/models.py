from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)
    inPower = models.CharField(max_length=64)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Promise(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank = True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
