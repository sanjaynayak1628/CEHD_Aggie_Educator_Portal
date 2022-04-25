from django.urls import path
from .views import CoopView, CoopTimeLogSubmit, CoopStudentCurrent, CoopViewGet


urlpatterns = [
    path('email/<str:coop_email>/approve', CoopStudentCurrent.as_view(), name='coop'),
    path('email/<str:email>/submit/approve/<str:approve>', CoopTimeLogSubmit.as_view(), name='coop_appr'),
    # path('email/<str:coop_email>/prev', CoopStudentCurrent.as_view(), name='coop_appr'),

    path('email/<str:coop_email>/view', CoopView.as_view(), name='coop_view_initial'),
    path('email/<str:coop_email>/view/student/<str:student_email>', CoopViewGet.as_view(), name='coop_student'),
    path('email/<str:coop_email>/view/student/<str:student_email>/semester/<str:semester>',
         CoopViewGet.as_view(), name='coop_student_sem'),

    path('email/<str:coop_email>/view/student/<str:student_email>/semester/<str:semester>/year/<str:year>',
         CoopViewGet.as_view(), name='coop_student_sem_year'),

    path('email/<str:coop_email>/view/student/<str:student_email>/year/<str:year>',
         CoopViewGet.as_view(), name='coop_student_year'),

    path('email/<str:coop_email>/view/student/<str:student_email>/start/<str:start_date>/end/<str:end_date>',
         CoopViewGet.as_view(), name='coop_student_dates'),

    path('email/<str:coop_email>/view/student/<str:student_email>/semester/<str:semester>/start/<str:start_date>/end/<str:end_date>',
         CoopViewGet.as_view(), name='coop_student_sem_dates'),

    path('email/<str:coop_email>/view/student/<str:student_email>/semester/<str:semester>/year/<str:year>/start/<str:start_date>/end/<str:end_date>',
        CoopViewGet.as_view(), name='coop_student_sem_dates_year'),

    path('email/<str:coop_email>/view/student/<str:student_email>/year/<str:year>/start/<str:start_date>/end/<str:end_date>',
        CoopViewGet.as_view(), name='coop_student_year_dates'),

]
