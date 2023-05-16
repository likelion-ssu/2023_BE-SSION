from django.shortcuts import render
from empApp.models import Employee

def employeeData(request):
    employees =Employee.objects.all()
    empDict = {"employees": employees}
    return render(request, 'employeeTemplates.html', empDict)

# Create your views here.
