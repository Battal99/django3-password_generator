from django.shortcuts import render
import django.http
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopkrstuvwxyz')
    the_password = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPKRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(*()?|{:"}'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))

    for _ in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def description(request):
    return render(request, 'generator/description.html')
