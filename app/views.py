from django.shortcuts import render,HttpResponse

# Create your views here.


def home(request):
    return render(request, "app/dashboard.html")

def product(request):
    return render(request, "app/product.html")

def customer(request):
    return render(request, "app/customer.html")