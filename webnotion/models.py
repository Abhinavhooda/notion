from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.

class availableservices(models.Model):
    availableservices_title = models.CharField(max_length=50, null=True, blank=False)
    availableservices_subtitile = models.CharField(max_length=50, blank=False, null=True)
    availableservices_desc = RichTextField(blank=False)
    availableservices_tags = RichTextField(blank=False)
    availableservices_url  = models.CharField(null=True,blank=False, max_length=200)


class Newsletter(models.Model):
    email = models.EmailField(max_length=40, blank= False)

class contact_form(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=60,null=True)
    phone = models.IntegerField(null=True)
    subject = models.CharField(max_length = 200, null=True)
    message = models.CharField(max_length = 2000,null=True)

class Blog(models.Model):
    blog_title = models.CharField(max_length=200,null=False,blank=False)
    blog_img = models.ImageField(upload_to='media', blank=False)
    blog_date = models.DateField(auto_now_add=False)
    blog_desc = RichTextField(blank=False)
    blog_slug = AutoSlugField(populate_from='blog_title', unique=True, default=None, blank=False, null=True)