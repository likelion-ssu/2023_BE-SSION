from django.shortcuts import render
from empApp.models import Emoployee

def employeeData(request):
    employees = Emoployee.objects.all()
    empDict = {'employees': employees}
    return render(request, 'employeeTemplates.html', empDict)

# Create your views here.
