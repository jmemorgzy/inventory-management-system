"""
inventory_management_system URL Configuration
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from users import views as user_views

urlpatterns = [
    path("", include("home.urls")),
    path("inventory/", include('inventory.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path("register_success/", user_views.register_success, name='register_success'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
