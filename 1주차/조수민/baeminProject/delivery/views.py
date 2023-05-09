from django.shortcuts import render
from django.http import HttpResponse

def delivery(request):
    return HttpResponse("<h1>배송과 관련된 정보를 보여주는 페이지입니당</h1>")

# Create your views here.
