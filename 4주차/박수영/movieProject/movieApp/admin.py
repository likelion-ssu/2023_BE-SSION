from django.contrib import admin
from movieApp.models import Movie
from movieApp.models import Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)