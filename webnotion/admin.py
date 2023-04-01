from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(contact_form)
class contactform(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','message')

@admin.register(Newsletter)
class NewsletterModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']

@admin.register(availableservices)
class availableservices(admin.ModelAdmin):
    list_display = ['id', 'availableservices_title','availableservices_desc','availableservices_url','availableservices_tags','availableservices_subtitile']
    