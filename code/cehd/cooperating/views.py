"""
views file describing the APIs used in coop time sheet API
"""
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from utils.emails import timesheet_approve, timesheet_reject


class CoopViews(APIView):
    """
    GET function to view the coop time sheets from the DB
    """

    def get(self, request, email, start_date=None, end_date=None, semester=None, approved=None, year=None):
        """
        GET function implementation
        """
        return render(request, f'cooperating/cooperatingview.html', status=status.HTTP_200_OK)


class CoopSubmit(APIView):
    """
    POST function to approve/reject the coop time sheets to the DB
    """

    def post(self, request, approve):
        print(request.data)
        # uncomment later after completion
        # if approve == "true":
        #     timesheet_approve()
        # else:
        #     timesheet_reject()
        return render(request, f'cooperating/cooperatingview.html', status=status.HTTP_200_OK)
