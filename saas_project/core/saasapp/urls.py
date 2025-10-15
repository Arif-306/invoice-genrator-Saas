from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-invoice/', views.create_invoice, name='create_invoice'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    # optional: add success/cancel pages if you want
    # path('success/', views.success, name='success'),
    # path('cancel/', views.cancel, name='cancel'),
]
