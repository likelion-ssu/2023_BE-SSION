from django.shortcuts import render
from django.http import HttpResponse

def delivery(request):
    return HttpResponse("<h1>delivery 페이지입니다.<h1>")

# Create your views here.
