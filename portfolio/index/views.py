from django.shortcuts import render
from .models import about


def home(request):
    aboutdata = about.objects.all()[0]
    context = {
        'about': aboutdata
    }
    return render(request, 'index.html', context)


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contact.html')
