from django.shortcuts import render
from .models import contactlist


# Create your views here.


def contactus(request):
    contactlistdata = contactlist.objects.all()[0]
    context = {
        'contactlist': contactlistdata
    }
    return render(request, 'contact.html', context)
