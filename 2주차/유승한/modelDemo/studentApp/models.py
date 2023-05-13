from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    studentId = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    grade = models.IntegerField()


