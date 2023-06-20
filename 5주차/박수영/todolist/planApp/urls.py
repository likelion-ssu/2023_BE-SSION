from django.urls import include, path
from planApp import views

urlpatterns = [
    path("<int:user_id>", views.Plans.as_view()),
    path("<int:user_id>/<int:plan_id>", views.PlanDetail.as_view()),
    path("<int:user_id>/<int:plan_id>/check", views.PlanCheck.as_view()),
    path("<int:user_id>/<int:plan_id>/reviews", views.PlanReview.as_view()),
]
