from django.urls import path, include
from .views import CoopViewsSave


urlpatterns = [
    # Student save time sheet URL
    path('cooperatingteacher/save/', CoopViewsSave.as_view(), name='coop_save_time_logs'),
    # student submit time sheet URL
]
