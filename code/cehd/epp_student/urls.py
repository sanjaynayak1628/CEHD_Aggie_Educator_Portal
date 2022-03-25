from django.urls import path
from .import views

urlpatterns = [
    path('student/', views.index, name='student'),
    path('accounts/profile/', views.index, name='profile'),
]
