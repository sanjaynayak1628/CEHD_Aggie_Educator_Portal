from django.shortcuts import render
import json
import datetime
from django.shortcuts import render
from django.core import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SupervisorView(APIView):
    """
    Get function to view the time sheets with co op and student view
    """
    def get(self, request, email):
        """
        GET function implementation
        """
        print(email, 'This is email from url')
        return render(request, f'supervisor/supervisorView.html')