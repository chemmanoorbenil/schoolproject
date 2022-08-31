from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import Depart

# Create your views here.
def department(request):
    department=Depart.objects.all()
    subject={
        'department':department
    }
    return render(request,"index.html",subject)


def login(request):
    return render(request,'login.html')



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        conform_password=request.POST['conform_password']
        user=User.objects.create_user(username=username,password=password)
        user.save();
        print("login")
    return render(request,'register.html')
def form(request):
    return render(request,'form.html')

