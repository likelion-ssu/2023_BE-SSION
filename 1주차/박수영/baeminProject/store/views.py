from django.shortcuts import render
from django.http import HttpResponse

def menu(request):
    return HttpResponse("<h1>메뉴판을 보여주는 페이지</h1>");

def order(request):
    return HttpResponse("<h1>음식을 주문하는 페이지</h1>");