from django.urls import path
from .views import CoopViews, CoopTimeLogSubmit, CoopStudentCurrent


urlpatterns = [
    path('email/<str:email>', CoopViews.as_view(), name='coop_view'),
    path('email/<str:email>/start/<str:start_date>/end/<str:end_date>/status/<str:approved>/semester/<str:semester>/year/<str:year>', CoopViews.as_view(), name='coop_reload'),
    path('submit/approve/<str:approve>/', CoopTimeLogSubmit.as_view(), name='coop_appr'),
    path('current/email/<str:coop_email>', CoopStudentCurrent.as_view(), name='coop_appr'),
]
