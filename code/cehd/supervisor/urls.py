from django.urls import path, include
from .views import SupervisorCoopView, SupervisorGet

urlpatterns = [
    # Supervisor time sheets view URL
    path('email/<str:email>', SupervisorCoopView.as_view(), name='supervisor_coop_view'),
    path('email/<str:email>/semester/<str:semester>', SupervisorCoopView.as_view(), name='supervisor_coop_view'),
    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>/start/<str:start_date>/end/<str:end_date>',
         SupervisorGet.as_view(), name='supervisor_get_time_logs_all'),
    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>',
         SupervisorGet.as_view(), name='supervisor_get_time_logs'),
    path('email/<str:super_email>/coop/<str:coop_email>/start/<str:start_date>/end/<str:end_date>',
         SupervisorGet.as_view(), name='supervisor_get_time_logs'),
    path('email/<str:super_email>/coop/<str:coop_email>/semester/<str:semester>/year/<str:year>/start/<str:start_date>',
         SupervisorGet.as_view(), name='supervisor_get_time_logs')
]