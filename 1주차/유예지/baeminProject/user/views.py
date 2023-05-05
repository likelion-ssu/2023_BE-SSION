from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display3(request):
    return HttpResponse('유저 앱')
