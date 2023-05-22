from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    active=models.BooleanField(default=True)
    running_time=models.IntegerField()

    def __str__(self):
        return self.title

