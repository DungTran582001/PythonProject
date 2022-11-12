from django.urls import path
from . import views


urlpatterns = [
    path("", view=views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", view=views.register, name="register"),
]