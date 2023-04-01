from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=40, blank= False)

class contact_form(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=60,null=True)
    phone = models.IntegerField(null=True)
    subject = models.CharField(max_length = 200, null=True)
    message = models.CharField(max_length = 2000,null=True)
