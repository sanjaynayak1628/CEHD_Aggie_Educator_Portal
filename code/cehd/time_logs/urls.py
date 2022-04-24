from django.urls import path, include
from .views import TimeLogViewsSave, TimeLogViewsSubmit, TimeLogViewsUinGet, TimeLogViewsEmailGet


urlpatterns = [
    # Student save time sheet URL
    path('save/', TimeLogViewsSave.as_view(), name='student_save_time_logs'),
    # student submit time sheet URL
    path('submit/', TimeLogViewsSubmit.as_view(), name="student_submit_time_logs"),
    # Student delete URLs from student UIN
    path('remove/uin/<int:student_uin>/date/<str:log_date>', TimeLogViewsSave.as_view(),
         name='student_delete_time_logs'),
    # Student get URLs from student UIN
    path('uin/<int:uin>', TimeLogViewsUinGet.as_view(), name='student_uin_get_time_logs'),
    path('uin/<int:uin>/semester/<str:semester>', TimeLogViewsUinGet.as_view(), name='student_uin_sem_get_time_logs'),
    path('uin/<int:uin>/start/<str:start_date>', TimeLogViewsUinGet.as_view(), name='student_uin_start_get_time_logs'),
    path('uin/<int:uin>/start/<str:start_date>/end/<str:end_date>', TimeLogViewsUinGet.as_view(),
         name='student_uin_startend_get_time_logs'),
    # Student get URLs from student email
    path('email/<str:email>', TimeLogViewsEmailGet.as_view(), name='student_email_get_time_logs'),
    path('email/<str:email>/semester/<str:semester>', TimeLogViewsEmailGet.as_view(),
         name='student_email_sem_get_time_logs'),
    path('email/<str:email>/start/<str:start_date>', TimeLogViewsEmailGet.as_view(),
         name='student_email_start_get_time_logs'),
    path('email/<str:email>/start/<str:start_date>/end/<str:end_date>', TimeLogViewsEmailGet.as_view(),
         name='student_email_startend_get_time_logs'),

    path('email/<str:email>/prev/<int:prev>', TimeLogViewsEmailGet.as_view(), name='student_email_get_time_logs_prev'),
]
