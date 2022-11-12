from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request,"app/main.html")


def login(request):
    return render(request, "app/login.html")

def register(request):
    if request.method == "POST":
        print(request.POST.get('email'))
    return render(request, "app/register.html")

