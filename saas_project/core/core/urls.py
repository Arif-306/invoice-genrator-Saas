from django.contrib import admin
from django.urls import path
from saasapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('invoice/', views.create_invoice, name='invoice'),
]
from django.urls import path
from saasapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-invoice/', views.create_invoice, name='create_invoice'),  # ✅ New
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),  # ✅ New
]
