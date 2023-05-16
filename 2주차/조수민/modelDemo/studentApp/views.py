from django.shortcuts import render
from studentApp.models import Student

def studentdata(request):
    students = Student.objects.all()
    stuDict = {'students' : students}
    return render(request, 'students.html', stuDict)

# Create your views here.
