from django.urls import path, include
from .views import TimeLogViewsSave, TimeLogViewsUinGet, TimeLogViewsEmailGet


urlpatterns = [
    # Student save/submit time sheet URL
    path('student/save/', TimeLogViewsSave.as_view(), name='student_save_time_logs'),
    # Student delete URLs from student UIN
    path('student/remove/uin/<int:student_uin>/date/<str:log_date>', TimeLogViewsSave.as_view(), name='student_delete_time_logs'),
    # Student get URLs from student UIN
    path('student/uin/<int:uin>', TimeLogViewsUinGet.as_view(), name='student_uin_get_time_logs'),
    path('student/uin/<int:uin>/semester/<str:semester>', TimeLogViewsUinGet.as_view(), name='student_uin_sem_get_time_logs'),
    path('student/uin/<int:uin>/start/<str:start_date>', TimeLogViewsUinGet.as_view(), name='student_uin_start_get_time_logs'),
    path('student/uin/<int:uin>/start/<str:start_date>/end/<str:end_date>', TimeLogViewsUinGet.as_view(), name='student_uin_startend_get_time_logs'),
    # Student get URLs from student email
    path('student/email/<str:email>', TimeLogViewsEmailGet.as_view(), name='student_email_get_time_logs'),
    path('student/email/<str:email>/semester/<str:semester>', TimeLogViewsEmailGet.as_view(), name='student_email_sem_get_time_logs'),
    path('student/email/<str:email>/start/<str:start_date>', TimeLogViewsEmailGet.as_view(), name='student_email_start_get_time_logs'),
    path('student/email/<str:email>/start/<str:start_date>/end/<str:end_date>', TimeLogViewsEmailGet.as_view(), name='student_email_startend_get_time_logs'),
]
