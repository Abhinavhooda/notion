from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.utils.translation import gettext as _
# from django.utils.translation import activate, get_language, gettext

def home(request):
    return render(request, 'webnotion/index.html', {})

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
    
def contactform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')   
        message = request.POST.get('message')   
        state = request.POST.get('state')   
        pincode = request.POST.get('pincode')   
        CF =  contact_form(name=name,email=email,phone=phone,subject=subject,message=message,)
        CF.save()
        messages.success(request,"Successfully Submitted")
        return redirect('contactform')
    return render(request,"rajapp/contact.html")
    
def handler404(request,*args,**argv):
    return render(request,'base/error.html')