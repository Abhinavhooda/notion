from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(contact_form)
class contact_form(admin.ModelAdmin):
    list_display = ('name','email','phone','subject','message')

@admin.register(Newsletter)
class NewsletterModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']

@admin.register(availableservices)
class availableservices(admin.ModelAdmin):
    list_display = ['id', 'availableservices_title','availableservices_desc','availableservices_url','availableservices_tags','availableservices_subtitile']

@admin.register(Blog)
class blog(admin.ModelAdmin):
    search_fields=[
        'id',
        'blog_title',
    ]
    list_display=['blog_title','id','blog_img','blog_desc']

@admin.register(Team)
class team(admin.ModelAdmin):
    search_fields=[
        'id',
        'member_name'
    ]
    list_display=['member_number','member_name','member_designation']