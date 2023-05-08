from django.shortcuts import render
from django.http import HttpResponse

def order(request):
    return HttpResponse("<h1>order 페이지입니다.<h1>")

# Create your views here.
