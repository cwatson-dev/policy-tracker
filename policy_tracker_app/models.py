from __future__ import unicode_literals
import uuid
import os
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from policy_tracker_project.settings import MEDIA_ROOT

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)

class Country(models.Model):
    name = models.CharField(max_length=64, unique=True)
    inPower = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    background_image = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_ROOT, 'country_images')), blank = True)
    map_image = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_ROOT, 'map_images')), blank = True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)
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


class Policy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    country = models.ForeignKey(Country)
    status = models.CharField(max_length=64)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = 'Policies'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=UploadToPathAndRename(os.path.join(MEDIA_ROOT, 'profile_images')), blank = True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
