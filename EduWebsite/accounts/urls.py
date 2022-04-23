from django. urls import path
from . import views
urlpatterns =[
path("", views.accounts, name="accounts"),
#path(route, view, opt(kisayol ismi))
]