#from django.shortcuts import render
from django.http import *
# Create your views here.

def index(request):
    return HttpResponse('<h1><b>hello world</b></h1>')
