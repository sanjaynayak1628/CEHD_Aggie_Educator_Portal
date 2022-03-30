from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TimeLogsSerializer
from .models import TimeLogs
import datetime


class TimeLogViews(APIView):
    def post(self, request):
        print(request.data)
        time_log_serializer = TimeLogsSerializer(data=request.data)
        if time_log_serializer.is_valid():
            try:
                time_log_serializer.save()
                return Response({"status": "success", "message": "Entered time entries saved successfully",
                                 "data": time_log_serializer.data}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"status": "error ", "message": "Check if table is migrated/created",
                                 "data": time_log_serializer.data}, status=status.HTTP_501_NOT_IMPLEMENTED)
        else:
            return Response({"status": "error", "message": "Error in saving the time entries. Please try again.",
                             "data": time_log_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, start_date=None, end_date=None):
        if not start_date and not end_date:
            today = datetime.date.today()
            week_day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
            week_dates = {week_day[i]: dates[i] for i in range(7)}
            return Response({"status": "success", "message": "Entered time entries saved successfully",
                             "data": ""}, status=status.HTTP_200_OK)
