import email
import re
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth



# Create your views here.
def login(request):

    return render(request,"login.html")


def register(request):
    if request.method == "POST":
         first_name = request.POST["firstname"]
         last_name = request.POST["lastname"]
         username = request.POST["username"]
         
         e_mail = request.POST["email"]
         password1 = request.POST["password1"]
         password2 = request.POST["password2"]
      
         
         user=User.objects.create_user(user_name=username,first_name=first_name,last_name=last_name,email=email,password=password1)
         user.save()
         print("kullanıcı oluşturudu")
         return redirect("/")

    else:
        return render(request,"register.html")
