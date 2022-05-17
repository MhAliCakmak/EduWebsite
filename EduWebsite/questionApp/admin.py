from dataclasses import field
from django.contrib import admin

from questionApp.models import Question,Categories,Test
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from rangefilter.filters import  DateTimeRangeFilter
from questionApp.resources import QuestionResource
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
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
    prepopulated_fields={"question_slug":("title",)}
    list_per_page=25
    actions=('admin_verified',)
    date_hierarchy= "update_date"
    fields=(("title","question_slug"),("category",),"description",("is_active"),("level","answer"))
    

    def admin_verified  (self,request,queryset):
        count=queryset.update(admin_verified=True)
        self.message_user(request,f"{count} yayina alindi")

    admin_verified.short_description="Admin onaylaması al"

class C_sorumlusu(admin.ModelAdmin):#Category yönetimi için
    prepopulated_fields={"category_slug":("title",)}
    list_display=("title","section","soruSayisi")
    list_filter=(("title",DropdownFilter),)
    search_fields=("section",)
    ordering=("title","section")
    list_per_page=10
    inlines =(S_Inline,)

class T_sorumlusu(admin.ModelAdmin):
    prepopulated_fields={"test_slug":("title",)}
    
    list_display=("title","information","selected_soru","soruSayisi","is_active","image")
    list_filter=(("title",DropdownFilter),)
    
    def selected_soru(self,obj):
        html="<ul>"
        for question in obj.questions.all():
            html+="<li>"+question.title+"</li>"
        html+="</ul>"
        return mark_safe(html)    

admin.site.register(Question,S_sorumlusu)
admin.site.register(Categories,C_sorumlusu)
admin.site.register(Test,T_sorumlusu)
