# Generated by Django 4.1.7 on 2023-04-01 16:21

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnotion', '0003_availableservices_availableservices_subtitile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_img', models.ImageField(upload_to='media')),
                ('blog_date', models.DateField()),
                ('blog_desc', ckeditor.fields.RichTextField()),
                ('blog_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='blog_title', unique=True)),
            ],
        ),
    ]