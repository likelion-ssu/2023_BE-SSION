from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=150)
    studentId = models.CharField(max_length=300)
    age = models.IntegerField()



# Create your models here.
