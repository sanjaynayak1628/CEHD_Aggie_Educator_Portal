from django.urls import path, include
from .views import SupervisorView


urlpatterns = [
    # Supervisor time sheets view URL
    path('email/<str:email>/view/', SupervisorView.as_view(), name='supervisor_view_time_sheets'),
]