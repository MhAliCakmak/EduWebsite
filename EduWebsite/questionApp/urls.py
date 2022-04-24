from django. urls import path
from . import views
urlpatterns =[


#path(route, view, opt(kisayol ismi))
path("soru/",views.student,name="student"),
path("",views.welcome,name="welcome"),
]