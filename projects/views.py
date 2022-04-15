from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os
from urllib import response
from projects.models import Cards

# Create your views here.


def home(request):
    return render(request ,'home.html')

def about(request):
    return render(request ,'about.html')


def contact(request):
    context = { "File": Cards.objects.all()}
    return render(request ,'contact.html',context)


def testimon(request):
    return render(request ,'home.html')


def projects(request):
    return render(request ,'projects.html')
    