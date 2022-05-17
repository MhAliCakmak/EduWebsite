from django. urls import path
from . import views
urlpatterns =[


#path(route, view, opt(kisayol ismi))
path("test_list/",views.test_list,name="test_list"),
path("<slug:test_slug>",views.test_detail,name="test_detail"),
path("<slug:test_slug>/<slug:question_slug>",views.question,name="question"),
path("",views.welcome,name="welcome"),
]