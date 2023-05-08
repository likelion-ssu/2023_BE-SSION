from django.shortcuts import render
from django.http import HttpResponse

def user(request):
    return HttpResponse("<h1>user 페이지입니다.<h1>")

# Create your views here.
