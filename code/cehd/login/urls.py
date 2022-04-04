from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'login/logout.html'), name='logout'),
]
