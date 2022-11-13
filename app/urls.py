from django.urls import path
from . import views


urlpatterns = [
    path("", view=views.home, name="home"),
    path("login/", views.loginView, name="login"),
    path("register/", view=views.registerView, name="register"),
    path("logout/", view=views.logoutView, name="logout"),
]