from django.urls import path
from .views import CoopViews, CoopTimeLogSubmit, CoopStudentCurrent,CoopApprove


urlpatterns = [
    path('email/<str:coop_email>/approve', CoopStudentCurrent.as_view(), name='coop_view'),
    path('email/<str:email>/start/<str:start_date>/end/<str:end_date>/status/<str:approved>/semester/<str:semester>/year/<str:year>', CoopViews.as_view(), name='coop_reload'),
    path('email/<str:email>/submit/approve/<str:approve>', CoopTimeLogSubmit.as_view(), name='coop_appr'),
    path('email/<str:coop_email>/prev', CoopStudentCurrent.as_view(), name='coop_appr'),
    
]
