from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField




# Create your models here.


class Question(models.Model):
    title=models.CharField(max_length=250)
    
    
    description=RichTextField()
    category=models.ForeignKey(to="questionApp.Categories", related_name="questions",on_delete=models.CASCADE,null=True)
    level=models.PositiveIntegerField(max_length=5,default=5,null=2)
    is_active=models.BooleanField(default=False)
    admin_verified=models.BooleanField(default=False)
    add_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=True,blank=True)
    answer=models.CharField(max_length=1,null="A")

    class Meta:
        verbose_name="Soru"
        verbose_name_plural="Sorular"

    def __str__(self):
        return self.title


class Categories(models.Model):
    
    name=models.CharField(max_length=50)
    section=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False,null=True)
    
    class Meta:
        verbose_name="Kategori"
        verbose_name_plural="Kategoriler"

    def __str__(self):
        return f"{self.name}/{self.section}"
    
    @property
    def soruSayisi(self):
        number=self.questions.count()
        return number
