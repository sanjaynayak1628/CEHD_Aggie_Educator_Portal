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
         SupervisorCoopGet.as_view(), name='supervisor_coop_dates'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>/start/<str:start_date>/end/<str:end_date>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem_dates_year'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/start/<str:start_date>/end/<str:end_date>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem_dates'),

    # URLs for export data as csv functionality
    path('email/<str:super_email>/export/<str:export>', SupervisorCoopView.as_view(), name='supervisor_all_export'),
    path('email/<str:super_email>/coop/<str:coop_email>/export/<str:export>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_export'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/export/<str:export>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem_export'),

    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>/export/<str:export>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_sem_year_export'),

    path('email/<str:super_email>/coop/<str:coop_email>/year/<str:year>/export/<str:export>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_year_export'),

    path('email/<str:super_email>/coop/<str:coop_email>/start/<str:start_date>/end/<str:end_date>/export/<str:export>',
         SupervisorCoopGet.as_view(), name='supervisor_coop_dates_export'),

    path(
        'email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>/start/<str:start_date>/end/<str:end_date>/export/<str:export>',
        SupervisorCoopGet.as_view(), name='supervisor_coop_sem_dates_year_export'),

    path(
        'email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/start/<str:start_date>/end/<str:end_date>export',
        SupervisorCoopGet.as_view(), name='supervisor_coop_sem_dates_export'),
]
