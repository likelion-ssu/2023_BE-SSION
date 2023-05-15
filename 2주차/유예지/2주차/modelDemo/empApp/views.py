from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def employeedata(request):
    employees=Employee.objects.all() #select *from empApp_employee
    empDict={'employees':employees}
    return render(request,'employees.html',empDict)