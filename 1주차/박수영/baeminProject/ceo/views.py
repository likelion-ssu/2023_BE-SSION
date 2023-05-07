from django.shortcuts import render
from django.http import HttpResponse

def plan(request):
    return HttpResponse("<h1>배민의 배달 대행 서비스 요금제를 선택하는 페이지</h1>");

def order(request):
    return HttpResponse("<h1>배민 앱을 통해 들어온 주문을 접수하는 페이지</h1>")