from django import forms
from .models import Question
from django.contrib.auth.models import User,auth
from django.forms import ModelForm


ANSWER_CHOICES =(
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),


)
class QuestionForm(forms.ModelForm):
    
    
    
      
    user_answer=forms.ChoiceField(choices=ANSWER_CHOICES,widget=forms.Select(attrs={'class':'form-select'}) )
    
    class Meta:
        model=Question
        
        fields="__all__"
    
    