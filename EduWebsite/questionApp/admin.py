from dataclasses import field
from django.contrib import admin
from questionApp.models import Question,Categories
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from rangefilter.filters import  DateTimeRangeFilter
from questionApp.resources import QuestionResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class S_Inline(admin.TabularInline):#Sorular yönetimi için
    model = Question
    fields = ("title","description","answer")
    extra=1
    classes=("collapse",)



class S_sorumlusu(ImportExportModelAdmin):
    list_display=("title",'category',"description",'admin_verified',"add_date","is_active")
    resource_class = QuestionResource
    list_filter=(
        ("category" ,RelatedDropdownFilter),
        ("add_date",DateTimeRangeFilter),
    )
    ordering=("title","-update_date")
    list_editable=("is_active",)
    search_fields=("title",)
    prepopulated_fields={"slug":("title",)}
    list_per_page=50
    actions=('admin_verified',)
    date_hierarchy= "update_date"
    fields=(("title","slug"),"category","description",("is_active","admin_verified"),("level","answer"))

    def admin_verified  (self,request,queryset):
        count=queryset.update(admin_verified=True)
        self.message_user(request,f"{count} yayina alindi")

    admin_verified.short_description="Admin onaylaması al"

class C_sorumlusu(admin.ModelAdmin):#Category yönetimi için
    
    list_display=("name","section","soruSayisi")
    list_filter=(("name",DropdownFilter),)
    search_fields=("section",)
    ordering=("name","section")
    list_per_page=10
    inlines =(S_Inline,)
    
admin.site.register(Question,S_sorumlusu)

admin.site.register(Categories,C_sorumlusu)