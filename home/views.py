from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
# Create your views here.

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if pass1 != pass2:
            return HttpResponse('password do not match with confirm password!!')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        return redirect("loginuser")

    return render(request, "signup.html")


def loginuser(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate( username = loginusername,password = loginpass)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
             return render(request,"loginuser.html")
    return render(request,"loginuser.html")

def dashboard(request):
    return render(request,"dashboard.html")