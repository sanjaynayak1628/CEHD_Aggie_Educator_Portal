from django.urls import path, include, re_path
from .views import StudentPlacementsGet


urlpatterns = [
    path('sp-get/<str:email>', StudentPlacementsGet.as_view(), name="view_details_email"),
    path('sp-get/<str:email>/<str:semester>', StudentPlacementsGet.as_view(), name="view_details_email_sem"),
]