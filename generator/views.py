from django.shortcuts import render
from django.http import HttpResponse 
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    psw = ""
    character = list("abcdefghilmnopqrstuvzwxyk")

    if request.GET.get("uppercase"):
        character.extend("QWERTYUIOPASDFGHJKLZXCVBNM")
    if request.GET.get("special"):
        character.extend("'!£$%&/()=")
    if request.GET.get("numbers"):
        character.extend("1234567890")
    
    lenght = int(request.GET.get("lenght",12))


    for x in range(lenght):
        psw += random.choice(character)
    return render(request, 'generator/password.html', {"password": psw})