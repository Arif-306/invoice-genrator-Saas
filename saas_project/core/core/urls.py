from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('saasapp.urls')),  # <-- Replace your_app_name with actual app name
]
