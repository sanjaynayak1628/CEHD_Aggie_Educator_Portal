from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from .serializers import TimeLogsSerializer
from .models import TimeLogs
from core.models import Person
import json
import datetime


class TimeLogViewsSave(APIView):
    def post(self, request):
        request_status_fail = list()
        response_data = list()
        response_status_list = list()
        for request_data in request.data.get("data", []):
            # print(request_data)
            time_log_serializer = TimeLogsSerializer(data=request_data)
            if time_log_serializer.is_valid():
                try:
                    # update the entries, if UIN and log date present pr create a new one
                    kwargs = {"student_uin": Person.objects.get(uin=request_data["student_uin"]), "log_date": request_data["log_date"]}
                    tmp = dict(request_data)
                    tmp.pop("student_uin", None)
                    tmp.pop("log_date", None)
                    obj, created = TimeLogs.objects.update_or_create(defaults=tmp, **kwargs)
                    tmp = request_data
                    tmp['created'] = created
                    response_data.append(tmp)
                except Exception as e:
                    print("Exception: {}".format(e))
                    request_status_fail.append(request_data.get("log_date", None))
            else:
                print(time_log_serializer.errors)
                request_status_fail.append(request_data.get("log_date", None))
        if request_status_fail:
            return Response({"status": "error", "message": "Time entered for dates: {} are not saved/submitted. "
                            "Please resave/resubmit again!".format(", ".join(
                                request_status_fail)), "data": response_data}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"status": "success",
             "message": "Entered {} time entries saved/updated successfully".format(len(request.data.get("data", []))),
             "data": response_data}, status=status.HTTP_200_OK)

    def delete(self, request, student_uin=None, log_date=None):
        try:
            item = TimeLogs.objects.get(student_uin=student_uin, log_date=log_date)
            item_serializer = TimeLogsSerializer(item)
            item.delete()
            return Response({"status": "success", "message": "Delete successful", "data": item_serializer.data}, status=status.HTTP_200_OK)
        except TimeLogs.DoesNotExist:
            return Response({"status": "not found", "message": "Delete unsuccessful", "data": {"student_uin": student_uin, "log_date": log_date}}, status=status.HTTP_204_NO_CONTENT)


class TimeLogViewsGet(APIView):
    def get(self, request, uin, start_date=None, end_date=None):
        if not start_date and not end_date:
            today = datetime.date.today()
            week_day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
            week_dates = {week_day[i]: dates[i] for i in range(7)}
            return Response({"status": "success", "message": "Retrieval successful", "data": week_dates}, status=status.HTTP_200_OK)
        elif not end_date:
            today = datetime.date.today()
            print(start_date)
            return Response({"status": "success", "message": "start date only given", "data": ""}, status=status.HTTP_200_OK)
        else:
            print(start_date, end_date)
            return Response({"status": "success", "message": "start date and end date given", "data": ""}, status=status.HTTP_200_OK)
