from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(contact_form)
class co_ntactform(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','message')

@admin.register(Newsletter)
class NewsletterModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']