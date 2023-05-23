from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=50)
    running_time = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.title