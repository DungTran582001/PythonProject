from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request,"app/main.html")


def login(request):
    return render(request, "app/login.html")

def register(request):
    return render(request, "app/register.html")

