from django.urls import path, include
from .views import CoopViews,CoopSubmit


urlpatterns = [
    # Student save time sheet URL
    path('cooperatingteacher/view/email/<str:email>', CoopViews.as_view(), name='coop_view'),
    # student submit time sheet URL
    path('cooperatingteacher/view/email/<str:email>/start/<str:start_date>/end/<str:end_date>/status/<str:status>/semester/<str:semester>', CoopViews.as_view(), name='coop_reload'),
    path('cooperatingteacher/submit/approve/<str:approve>/', CoopSubmit.as_view(), name='coop_appr'),
    


]
