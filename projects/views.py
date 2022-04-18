from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os
from urllib import response
from projects.models import Cards,Form

# Create your views here.


def home(request):
    return render(request ,'home.html')

def about(request):
    return render(request ,'about.html')


def contact(request):
    if request.method =="POST":
        form = Form()
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email= request.POST.get('email')
        message= request.POST.get('message')
        form.FistName = fname
        form.LastName = lname
        form.Email = email
        form.Message = message
        form.save()
       
        return HttpResponse('<h1>Your form has been submitted successfully </h1>')
    return render(request ,'contact.html')
    
   


def testimon(request):
    return render(request ,'testimon.html')


def projects(request):
    context = { "File": Cards.objects.all()}
    return render(request ,'projects.html',context)
    