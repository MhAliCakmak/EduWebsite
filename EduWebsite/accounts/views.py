import email
import re

# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)

        if user is not None:
            first_name=user.first_name
            auth_login(request,user)  
            messages.success(request,"Giris Basarılı")
            return redirect("test_list")            
        else:
            messages.error(request,"Bad Credentials")
            return redirect("login")
    return render(request,"login.html")


def register(request):
    
    if request.method == "POST":
         first_name = request.POST["first_name"]
         last_name = request.POST["last_name"]
         username = request.POST["username"]
         email = request.POST["email"]
         password1 = request.POST["password1"]
         password2 = request.POST["password2"]
         user_type=request.POST["user_type"]
        
         if user_type=="Öğrenci":
            user=User.objects.create_user(first_name=first_name,username=username,last_name=last_name,email=email,password=password1)
            user.save()
            messages.success(request,"Your account has been successfully created")
            return redirect("login")
         
         elif user_type=="Admin":    
             user=User.objects.create_superuser(first_name=first_name,username=username,last_name=last_name,email=email,password=password1)
             user.save()
             messages.success(request,"Your account has been successfully created")
             return redirect("admin")
         
         elif user_type=="Sınav Sorumlusu":
             user=User.objects.create_user(first_name=first_name,username=username,last_name=last_name,email=email,password=password1,is_staff=True)
             return ("login")
         user.first_name=first_name
         user.last_name=last_name
         
         
         

    else:
        return render(request,"register.html")
@login_required
def logout(request):
    auth_logout(request)
    messages.success(request,"Başarılı çıkıs")
    return redirect("welcome")
