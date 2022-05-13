from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User




# Create your models here.


class Question(models.Model):
    title=models.CharField(max_length=250)
    
    
    description=RichTextField()
    category=models.ForeignKey(to="questionApp.Categories", related_name="questions",on_delete=models.CASCADE,null=True)
    
    level=models.PositiveIntegerField(default=5,null=2)
    is_active=models.BooleanField(default=False)
    admin_verified=models.BooleanField(default=False)
    add_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    question_slug=models.SlugField(null=True,blank=True)
    answer=models.CharField(max_length=1,null="A")

    class Meta:
        verbose_name="Soru"
        verbose_name_plural="Sorular"

    def __str__(self):
        return self.title


class Categories(models.Model):
    
    title=models.CharField(max_length=50)
    section=models.CharField(max_length=50)
    
    is_active=models.BooleanField(default=False,null=True)
    category_slug=models.SlugField(null=True,blank=True)

    class Meta:
        verbose_name="Kategori"
        verbose_name_plural="Kategoriler"

    def __str__(self):
        return f"{self.title}/{self.section}"
    
    @property
    def soruSayisi(self):
        number=self.questions.count()
        return number

class Test(models.Model):
    title=models.CharField(max_length=50)
    information=models.TextField(max_length=250,default="Fen Bilimleri dersi standart sorular",null=True)
    test_slug=models.SlugField(null=True,blank=True)
    questions=models.ManyToManyField(Question)
    is_active=models.BooleanField(default=False,null=True)
    image=models.ImageField(upload_to="static/Test")
    user=models.ManyToManyField(User,blank=True,related_name="Test_joined")
    class Meta:
        verbose_name="Test"
        verbose_name_plural="Testler"

    def __str__(self):
        return f"{self.title}"    
    @property
    def soruSayisi(self):
        number=self.questions.count()
        return number
    