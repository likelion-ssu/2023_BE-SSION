from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse("<h1>회원가입 페이지입니당</h1>")

def login(request):
    return HttpResponse("<h1>로그인 페이지입니당</h1>")

# Create your views here.
