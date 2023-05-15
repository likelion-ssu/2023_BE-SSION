from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10)
    studentId=models.IntegerField()
    age=models.IntegerField()
    major=models.CharField(max_length=15)