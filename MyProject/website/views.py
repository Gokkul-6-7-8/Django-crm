from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records=Record.objects.all()


    if request.method == 'POST':
        yourName = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=yourName, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "There is an error!")
            return redirect('home')
    else:  
        return render(request, 'index.html',{'records':records})
    
def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out successfully")
    return redirect('home')

def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()

        username=form.cleaned_data['username']
        password1=form.cleaned_data['password1']
        user=authenticate(username=username,password=password1)
        login(request,user)
        messages.success(request,"You have been registered")
        return redirect('home')
    else:
        form=SignUpForm()
    return render(request,'register.html', {'form':form})