import imp
from tkinter import Y
from django.shortcuts import render

# Create your views here.
def sayHello(request):
    return render(request, 'index.html', {'name':'Sed'})


