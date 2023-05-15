from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=15)
    salary=models.IntegerField()
    email=models.CharField(max_length=35)