
from django.urls import path
from movieapp import views

urlpatterns = [
    path('',views.movie_list),
    path('<int:id>/',views.movie_details),
]
