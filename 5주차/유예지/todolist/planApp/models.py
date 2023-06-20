from django.db import models
from userApp.models import User
# Create your models here.

class Plan(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField()
    content=models.TextField()
    is_checked=models.BooleanField(default=False)
    emoji=models.CharField(
        max_length=1, #이모지 하나만
        default="", #없으면 디폴트값 줘라
        blank=True #값 없어도 어드민 페이지에서 에러 발생하지 않음
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.content
