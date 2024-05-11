from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html',{})

def login_user(request):
    pass

def logout_user(request):
    pass
