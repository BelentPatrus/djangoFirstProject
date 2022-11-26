from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def authlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid password and username")

    return render(request, 'authentication/login.html')


def authregistration(request):
    return render(request, 'authentication/register.html')


def forgetpassword(request):
    return render(request, 'authentication/forget.html')


def authlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')
