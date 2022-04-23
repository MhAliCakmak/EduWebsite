from django.contrib import admin
from questionApp.models import Question
# Register your models here.
import faker
class S_sorumlusu(admin.ModelAdmin):
    list_display=("title",'description','admin_verified',"add_date")
    list_filter=("admin_verified","add_date")
    ordering=("title","-update_date")
    search_fields=("title",)
    prepopulated_fields={"slug":("title",)}
admin.site.register(Question,S_sorumlusu)

