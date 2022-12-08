import os
from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse

from subprocess import run,PIPE
import sys
# Create your views here.

def home(request):
    return render(request, "home.html")

def button(request):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    temp="\img2txt\img_to_txt.py"
    location=desktop+temp
    
    run([sys.executable,location], shell=False,stdout=PIPE)

    return render(request,"home.html")