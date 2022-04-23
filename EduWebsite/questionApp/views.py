from django.shortcuts import render
from questionApp.models import Question
# Create your views here.
def index(request):
    context={
        "Question" : Question.objects.all()
    }
    return render(request,)