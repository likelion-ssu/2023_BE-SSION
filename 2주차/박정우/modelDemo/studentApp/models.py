from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    grade = models.IntegerField()
    number = models.IntegerField()
    age = models.IntegerField()