from django.urls import path, include
from .views import TimeLogViewsSave, TimeLogViewsGet


urlpatterns = [
    path('student/save/', TimeLogViewsSave.as_view(), name='student_save_time_logs'),
    path('student/remove/uin/<int:student_uin>/date/<str:log_date>', TimeLogViewsSave.as_view(), name='student_delete_time_logs'),
    path('student/uin/<int:uin>', TimeLogViewsGet.as_view(), name='student_get_time_logs'),
    path('student/uin/<int:uin>/start/<str:start_date>', TimeLogViewsGet.as_view(), name='student_get_time_logs'),
    path('student/uin/<int:uin>/start/<str:start_date>/end/<str:end_date>', TimeLogViewsGet.as_view(), name='student_get_time_logs'),
]
