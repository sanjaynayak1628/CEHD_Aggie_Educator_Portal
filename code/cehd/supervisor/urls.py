from django.urls import path
from .views import SupervisorCoopView, SupervisorCoopGet

urlpatterns = [
    # Supervisor time sheets view URL
    path('email/<str:super_email>', SupervisorCoopView.as_view(), name='supervisor_coop_view'),
    path('email/<str:super_email>/coop/<str:coop_email>',
         SupervisorCoopGet.as_view(), name='supervisor_coop'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem_year'),

    path('email/<str:super_email>/coop/<str:coop_email>/year/<str:year>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_year'),

    path('email/<str:super_email>/coop/<str:coop_email>/start/<str:start_date>/end/<str:end_date>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_st_end'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>/start/<str:start_date>/end/<str:end_date>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem_dates_year'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/start/<str:start_date>/end/<str:end_date>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem_dates'),
]
