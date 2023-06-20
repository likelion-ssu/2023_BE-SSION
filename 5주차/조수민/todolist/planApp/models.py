from django.db import models
from userApp.models import User

class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField() #datetime 이 시간까지 나옴 년월일이랑
    content = models.TextField()
    is_checked = models.BooleanField(default=False)
    emogi = models.CharField(
        max_length=1,
        default="", #데이터 페이지에서 적용되는거
        blank=True #admin 페이지에서 이 값이 없어도 오류 안 나게

    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


# Create your models here.
