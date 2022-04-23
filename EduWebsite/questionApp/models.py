from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=250)
    image=models.CharField(max_length=50)
    description=RichTextField()
    is_active=models.BooleanField(default=False)
    admin_verified=models.BooleanField(default=False)
    add_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=True,blank=True)

    class Meta:
        verbose_name="Soru"
        verbose_name_plural="Sorular"

    def __str__(self):
        return self.title