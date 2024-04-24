from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo = "¡Hello world!"
    return HttpResponse(saludo)

def about(request):
    return HttpResponse('About')