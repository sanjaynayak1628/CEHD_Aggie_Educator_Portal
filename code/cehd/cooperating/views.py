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





class CoopViews(APIView):
    """
    GET function to view the coop time sheets from the DB
    """
    def get(self, request, email, start_date=None, end_date=None, semester=None, status=None):
        """
        GET function implementation
        """
        print(f'{email}--{start_date}--{end_date}--{semester}--{status}')
        return render(request, f'cooperating/cooperatingview.html')

class CoopSubmit(APIView):
    """
    POST function to approve/reject the coop time sheets to the DB
    """
    def post(self, request, approve):
        print(approve)
        return render(request, f'cooperating/cooperatingview.html')
