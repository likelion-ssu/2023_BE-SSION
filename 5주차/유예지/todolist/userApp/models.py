from django.db import models

# Create your models here.
class User(models.Model): #장고 제공 클래스 상속이 베스트
    username=models.CharField(
        max_length=150,
        unique=True #중복 방지
    )
    password=models.CharField(
        max_length=150
    )
    def __str__(self):
        return self.username