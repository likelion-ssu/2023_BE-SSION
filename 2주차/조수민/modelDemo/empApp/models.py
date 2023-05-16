from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=150)
    salary = models.IntegerField()
    phone_number = models.CharField(max_length=30) 
    email = models.CharField(max_length=150)

# Create your models here.
