from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', views.login_view, name='login'),
    path('invoice/', views.generate_invoice, name='invoice'),
]
