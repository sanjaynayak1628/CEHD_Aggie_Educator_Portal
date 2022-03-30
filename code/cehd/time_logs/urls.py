from django.urls import path, include
from .views import TimeLogViews


urlpatterns = [
    path('save/', TimeLogViews.as_view(), name='save_time_logs')
]
