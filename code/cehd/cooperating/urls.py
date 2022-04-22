from django.urls import path
from .views import CoopViews, CoopSubmit


urlpatterns = [
    path('view/email/<str:email>', CoopViews.as_view(), name='coop_view'),
    path('view/email/<str:email>/start/<str:start_date>/end/<str:end_date>/status/<str:approved>/semester/<str:semester>/year/<str:year>', CoopViews.as_view(), name='coop_reload'),
    path('submit/approve/<str:approve>/', CoopSubmit.as_view(), name='coop_appr'),
]
