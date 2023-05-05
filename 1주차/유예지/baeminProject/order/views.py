from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display2(request):
    return HttpResponse('오더 앱')
