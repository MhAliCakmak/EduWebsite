from django. urls import path
from . import views
urlpatterns =[
path("", views.questionApp, name="Question"),
#path(route, view, opt(kisayol ismi))
]