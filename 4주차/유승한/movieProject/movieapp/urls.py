
from django.urls import path
from movieapp import views

urlpatterns = [
    path('',views.MovieListView.as_view()),
    path('<int:id>/',views.MovieDetailView.as_view()),
    path('<int:id>/reviews/',views.MovieReviewListView.as_view()),
    path('<int:id>/reviews/<int:review_id>/',views.MovieReviewDetailView.as_view()),
]
