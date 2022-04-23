from dataclasses import field
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
    list_per_page=50
    actions=('admin_verified',)
    date_hierarchy= "update_date"
    fields=("title","slug","description","is_active","answer")
    def admin_verified  (self,request,queryset):
        count=queryset.update(admin_verified=True)
        self.message_user(request,f"{count} yayina alindi")

    admin_verified.short_description="Admin onaylaması al"

admin.site.register(Question,S_sorumlusu)

