from django.contrib import admin
from django.urls import path,include


base_api_path = "api/v1/"


urlpatterns = [
    path('admin/', admin.site.urls),
    path(base_api_path, include('user.urls')),
]
