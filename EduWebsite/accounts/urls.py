from django. urls import path
from . import views
urlpatterns =[
path("", views.welcome, name="welcome"),
path("login/",views.accounts,name="accounts"),
path("register/",views.register,name="register"),

#path(route, view, opt(kisayol ismi))
]