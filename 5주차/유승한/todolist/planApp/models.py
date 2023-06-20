from django.db import models
from userApp.models import User

# Create your models here.
class Plan(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    content = models.TextField()
    is_checked = models.BooleanField(default=False)
    emoji = models.CharField(
        max_length=1,
        default="", #data base 디폴트
        blank=True  #admin page 디폴트
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    