import re
from django.shortcuts import render

# Create your views here.
def accounts(request):
    return render(request,"login.html")

def welcome(request):
    return render(request,"anasayfa.html")

def register(request):
    return render(request,"register.html")