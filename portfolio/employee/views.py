from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def employee(request):
    return HttpResponse("This is the employee Page")

def profile(request):
    return render(request,'employee/profile.html')
