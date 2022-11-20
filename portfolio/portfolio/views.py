from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    text = {
        'name': "Belent Patrus",
        'age': 23,
        'phone': 45454545,
        'friend_name': ['Belent', 'Patrus', 'Udemy', 'Billy']
    }
    return render(request, 'index.html', text)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
