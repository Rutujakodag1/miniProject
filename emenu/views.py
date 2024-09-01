from django.http import HttpResponse
# from django.contrib import redirects
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# from django.apps import table
# from table.models import Table,Order

def index(request):
    return render(request,'index.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Invalid user or password..')
            return render(request,'login.html')
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return render(request,'index.html')

