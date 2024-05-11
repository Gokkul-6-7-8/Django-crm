from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
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
        return render(request, 'index.html')
