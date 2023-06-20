from django.urls import include, path
from userApp import views

urlpatterns = [
  path("sign-up", views.SignUp.as_view()),
  path("log-in", views.LogIn.as_view()),
]