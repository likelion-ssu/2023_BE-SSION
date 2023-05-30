from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    active = models.BooleanField(default = True)
    running_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name = 'reviews')

    def __str__(self):
        return self.title

