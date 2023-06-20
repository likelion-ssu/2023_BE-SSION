from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include("userApp.urls")),
    path('api/plans/', include("planApp.urls")),
]
