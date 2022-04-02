from django.urls import path, include
from .views import TimeLogViewsSave, TimeLogViewsGet


urlpatterns = [
    path('student/', TimeLogViewsSave.as_view(), name='student_save_time_logs'),
    path('student/uin=<int:uin>', TimeLogViewsGet.as_view(), name='student_get_time_logs')
]
