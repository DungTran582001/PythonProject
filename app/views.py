from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Member,Expense,Income
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,"app/main.html")


def loginView(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            get_user_with_email = Member.objects.filter(email = request.POST.get('email')).first()
            if not get_user_with_email:
                pass
            else:
                user_auth = authenticate(request, username= get_user_with_email.name, password = request.POST.get("password"))
                if user_auth is not None:
                    login(request,user_auth)
                    return redirect("home")
                else:
                    pass
        return render(request, "app/login.html")

def registerView(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            if request.POST.get("email") == "" or request.POST.get("username") == "" or request.POST.get("password1") == "" or request.POST.get("password2") == "":
                messages_error = "Vui lòng điền đầy đủ thông tin."
                context = {"msg": messages_error}
                return render(request, "app/register.html", context)
            else:
                email_exist = Member.objects.filter(email = request.POST.get("email")).first()
                if not email_exist:
                    if request.POST.get("password1") == request.POST.get("password2"):
                        new_user = User.objects.create_user(username = request.POST.get("username"), password = request.POST.get("password1"))
                        Member.objects.create(user = new_user,name = request.POST.get("username"),email = request.POST.get("email"))
                        return redirect("login")
                    else:   
                        messages_error = "Mật khẩu và mật khẩu xác nhận không trùng khớp!"
                        context = {"msg": messages_error}
                        return render(request, "app/register.html", context)
                else:
                    messages_error = "Email đã được sử dụng. Vui lòng dùng email khác để đăng ký."
                    context = {"msg": messages_error}
                    return render(request, "app/register.html", context)
        context = {}
        return render(request, "app/register.html", context=context)

def logoutView(request):
    logout(request)
    return redirect("login")

