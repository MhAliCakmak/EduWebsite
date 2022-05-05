from multiprocessing import context
from django.shortcuts import render
from questionApp.models import Question,Test,Categories
 

# Create your views here.


def welcome(request):
    return render(request,"anasayfa.html")
def test_list(request):
    tests=Test.objects.all()
    context={
        "tests":tests
    }
    return render(request,"question.html",context)

def test_detail(request,test_slug):
    test=Test.objects.get(test_slug=test_slug)
   
    context={
        "test_detail":test,
        "question":test.questions.all(),
        
    }
    return render(request,"testGosterme.html",context)

def question(request,test_slug,quest_slug):
    test=Test.objects.get(test_slug=test_slug)
   
    context={
        "question":test.questions.get(question_slug=quest_slug),
        
    }
    return render(request,"soruTest.html",context)
