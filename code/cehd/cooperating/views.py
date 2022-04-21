"""
views file describing the APIs used in student time sheet API
"""
import json
import datetime
from django.shortcuts import render
from django.core import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response





class CoopViewsSave(APIView):
    """
    POST function to save the time sheets into the DB
    """
    def get(self, request):
        """
        POST function implementation
        """
        return render(request, f'cooperating/cooperatingview.html')

    