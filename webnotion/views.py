from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.utils.translation import gettext as _
# from django.utils.translation import activate, get_language, gettext
from django.views.decorators.cache import cache_control
from datetime import datetime, timedelta
@cache_control(max_age=86400, expires=datetime.utcnow() + timedelta(days=365))

def home(request):
    homeservices = availableservices.objects.all().order_by('id').reverse()
    hometeam = Team.objects.all().order_by('id')
    return render(request, 'webnotion/index.html', {'homeservices':homeservices,'hometeam':hometeam})

def about(request):
    return render(request, 'webnotion/about.html',{})   

def service(request):
    return render(request, 'webnotion/service.html',{})
     
def team(request):
    return render(request, 'webnotion/team.html', {})

def blog(request):
    return render(request, 'webnotion/blog.html', {})

def contact(request):
    return render(request, 'webnotion/contact.html', {})
       
def career(request):
    return render(request, 'webnotion/career.html', {})

def faqs(request):
    return render(request, 'webnotion/faqs', {})

def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        em = Newsletter.objects.create(email=email)
        em.save()
        return redirect('/')

class Services(View):
    def get(self, request):
        services =  availableservices.objects.all().order_by('id').reverse()
        return render(request, 'webnotion/service.html', {'services':services})

class Servicesdetailview(View):
    def get(self, request, slug):
        Service = availableservices.objects.get(availableservices_url=slug)
        service_object = availableservices.objects.get(availableservices_url=slug)
        service_object.save()
        return render(request, 'webnotion/service-detail.html', {'Service':Service})
        

class blogs(View):
    def get(self, request):
        blog = Blog.objects.all().order_by('id').reverse()
        return render(request, 'webnotion/blog.html', {'blog':blog})
    
class blogdetailview(View):
    def get(self, request, slug):
        blog = Blog.objects.get(blog_slug=slug)
        blog_object = Blog.objects.get(blog_slug=slug)
        blog_object.save()
        return render(request, 'webnotion/blog-detail.html', {'blog':blog})
        
class teammembers(View):
    def get(self, request):
        team = Team.objects.all().order_by('id').reverse()
        return render(request, 'webnotion/team.html', {'team':team})

class teamdetailview(View):
    def get(self, request, slug):
        team=Team.objects.get(member_slug=slug)
        team_object = Team.objects.get(member_slug=slug)
        team_object.save()
        return render(request, 'webnotion/team-detail.html', {'team':team})
        
def contactform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')   
        message = request.POST.get('message')    
        CF =  contact_form(name=name,email=email,phone=phone,subject=subject,message=message,)
        CF.save()
        messages.success(request,"Successfully Submitted")
        return redirect('contactform')
    return render(request,"webnotion/contact.html")
    
def handler404(request,exception):
    return render(request,'base/error.html')