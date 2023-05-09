from django.shortcuts import render
from django.http import HttpResponse

def order(request):
    return HttpResponse("<h1>주문과 관련된 정보를 보여주는 페이지입니당</h1>")

# Create your views here.
