from django.shortcuts import render
rom django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os
from urllib import response

# Create your views here.


def home(request):
    return render(request ,'projects/home.html')

def about(request):
    return render(request ,'projects/about.html')


def contact(request):
    return render(request ,'projects/contact.html')


def testimon(request):
    return render(request ,'projects/home.html')


def projects(request):
    return render(request ,'projects/proects.html')
    