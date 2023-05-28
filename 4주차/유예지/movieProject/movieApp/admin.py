from django.contrib import admin
from movieApp.models import Movie,Review

# Register your models here.
admin.site.register(Movie) #어드민 페이지 데이터 등록
admin.site.register(Review)