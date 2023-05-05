from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display1(request):
    return HttpResponse('딜리버리 앱')
