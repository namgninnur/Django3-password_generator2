from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'hui43g6iu304'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    charachters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        charachters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        charachters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charachters)

    return render(request, 'generator/password.html', {'password':thepassword})
