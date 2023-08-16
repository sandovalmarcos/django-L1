from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Home')


def sobre(request):
    return HttpResponse('Sobre')


def contacto(request):
    return HttpResponse('Contacto')
