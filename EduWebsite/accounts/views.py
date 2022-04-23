import re
from django.shortcuts import render

# Create your views here.
def accounts(request):
    return render(request,"login.html")