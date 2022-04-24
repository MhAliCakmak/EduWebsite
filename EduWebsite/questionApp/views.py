from multiprocessing import context
from django.shortcuts import render
from questionApp.models import Question,Test
# Create your views here.


def welcome(request):
    return render(request,"anasayfa.html")
def student(request):
    context={
        "test":Test.objects.all()
    }
    return render(request,"question.html",context)