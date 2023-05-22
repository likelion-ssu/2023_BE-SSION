from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=50) #영화제목
    description=models.CharField(max_length=200)#영화설명
    active=models.BooleanField(default=True)#상영여부
    running_time=models.IntegerField()#상영시간

    def __str__(self):
        return self.title