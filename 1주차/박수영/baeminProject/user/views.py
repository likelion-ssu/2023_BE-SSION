from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return HttpResponse("<h1>프로필 확인하는 페이지</h1>");

def order(request):
    return HttpResponse("<h1>사용자의 주문 내역을 확인하는 페이지</h1>");