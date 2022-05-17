from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404, HttpResponseRedirect
from .forms import QuestionForm
from questionApp.models import Question,Test,Categories
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.views.generic.edit import FormView
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



def question(request,test_slug,question_slug):
    test=Test.objects.get(test_slug=test_slug)
    obj = get_object_or_404(Question, question_slug = question_slug)
    question=test.questions.filter(question_slug=question_slug).values()
    form = QuestionForm(data=request.POST or None,instance=obj)
    if request.method == "POST":
        if form.is_valid():

            form.save()
            messages.success(request, "mesajınız başarıyla iletilmiştir")
           
            return HttpResponseRedirect(reverse("questions",args=(question.user_answer,)))
    
  
    context={
        "test_detail":test,
        "question":question,
        "form": form,
        
    }
 
   
    
    
        
    return render(request,"soruTest.html",context)
