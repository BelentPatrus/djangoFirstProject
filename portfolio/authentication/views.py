from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

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
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['Password']
        confirm_password = request.POST['confirm_pass']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username not available")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email not available")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('profile')

        else:
            messages.error(request, "fail")

    return render(request, 'authentication/register.html')


def forgetpassword(request):
    return render(request, 'authentication/forget.html')


def authlogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('login')
