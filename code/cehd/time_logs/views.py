from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from .serializers import TimeLogsSerializer
from .models import TimeLogs
from core.models import Person
from student_placements.views import query_student_placements_email, query_student_placements_uin
import json
import datetime


def save_time_logs(request):
    request_status_fail = list()
    response_data = list()
    response_status_list = list()
    for request_data in request.data.get("data", []):
        # print(request_data)
        time_log_serializer = TimeLogsSerializer(data=request_data)
        if time_log_serializer.is_valid():
            try:
                # update the entries, if UIN and log date present or create a new one
                kwargs = {"student_uin": Person.objects.get(uin=request_data["student_uin"]),
                          "log_date": request_data["log_date"]}
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
    return response_data, request_status_fail


class TimeLogViewsSubmit(APIView):
    def post(self, request):
        response_data, request_status_fail = save_time_logs(request)
        response_dict = dict()
        status_mode = status.HTTP_200_OK
        if request_status_fail:
            response_dict["status"] = "error"
            response_dict["message"] = "Time entered for dates: {} are not submitted. Please resubmit " \
                                       "again!".format(", ".join(request_status_fail))
            response_dict["data"] = response_data
            status_mode = status.HTTP_400_BAD_REQUEST
        else:
            response_dict["status"] = "success"
            response_dict["message"] = "Entered {} time entries submitted successfully".format(len(request.data.get("data", [])))
            response_dict["data"] = response_data
            # send the email to cooperating teacher
            cooperating_teacher_email = request.data.get("cooperating_teacher_email", "")
            cooperating_teacher_name = request.data.get("cooperating_teacher_name", "")
            if cooperating_teacher_email == "":
                response_dict["status"] = "error"
                status_mode = status.HTTP_403_FORBIDDEN
                response_dict["message"] = "Entered time not submitted. Co-operating teacher not found. Please save the time entries."
        return Response(response_dict, status=status_mode)


class TimeLogViewsSave(APIView):
    def post(self, request):
        response_data, request_status_fail = save_time_logs(request)
        if request_status_fail:
            return Response({"status": "error", "message": "Time entered for dates: {} are not saved. "
                             "Please resave again!".format(", ".join(request_status_fail)), "data": response_data}, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"status": "success",
             "message": "Entered {} time entries saved successfully".format(len(request.data.get("data", []))),
             "data": response_data}, status=status.HTTP_200_OK)

    def delete(self, request, student_uin=None, log_date=None):
        try:
            item = TimeLogs.objects.get(student_uin=student_uin, log_date=log_date)
            item_serializer = TimeLogsSerializer(item)
            item.delete()
            return Response({"status": "success", "message": "Delete successful", "data": item_serializer.data},
                            status=status.HTTP_200_OK)
        except TimeLogs.DoesNotExist:
            return Response({"status": "not found", "message": "Delete unsuccessful",
                             "data": {"student_uin": student_uin, "log_date": log_date}},
                            status=status.HTTP_404_NOT_FOUND)


def query_timelog_uin(uin, start_date, end_date):
    saved_time = TimeLogs.objects.all().filter(student_uin=uin, log_date__lte=end_date,
                                               log_date__gte=start_date).order_by('log_date')
    saved_time_serializer = json.loads(serializers.serialize('json', saved_time))
    # print("Data: {}".format(saved_time_serializer))
    saved_data = dict()
    for sv_data in saved_time_serializer:
        if sv_data.get('fields', None):
            saved_data[sv_data['fields']['log_date']] = sv_data['fields']
    return saved_data


def query_timelog_email(email, start_date, end_date):
    saved_time = TimeLogs.objects.all().filter(student_email=email, log_date__lte=end_date,
                                               log_date__gte=start_date).order_by('log_date')
    saved_time_serializer = json.loads(serializers.serialize('json', saved_time))
    # print("Data: {}".format(saved_time_serializer))
    saved_data = dict()
    for sv_data in saved_time_serializer:
        if sv_data.get('fields', None):
            saved_data[sv_data['fields']['log_date']] = sv_data['fields']
    return saved_data


def query_sp_email(email, semester=None):
    sp_item_serializer = query_student_placements_email(email, semester)
    if len(sp_item_serializer) > 0:
        sp_item_serializer = sp_item_serializer[0]['fields']
    else:
        sp_item_serializer = dict()
    return sp_item_serializer


def query_sp_uin(uin, semester=None):
    sp_item_serializer = query_student_placements_uin(uin, semester)
    if len(sp_item_serializer) > 0:
        sp_item_serializer = sp_item_serializer[0]['fields']
    else:
        sp_item_serializer = dict()
    return sp_item_serializer


def get_current_week():
    # add current week dates
    today = datetime.date.today()
    dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
    week_day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    week_dates = {week_day[i]: dates[i] for i in range(7)}
    return week_dates


class TimeLogViewsUinGet(APIView):
    def get(self, request, uin, start_date=None, end_date=None, semester=None):
        message = ""
        if not start_date and not end_date:
            today = datetime.date.today()
            dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
            start_date = dates[0]
            end_date = dates[6]
            message = "retrieval successful for current week"
        elif not end_date:
            end_date = datetime.date.today()
            message = "start date only provided"
        else:
            print(start_date, end_date)
            message = "start date and end date provided"

        saved_data = query_timelog_uin(uin, start_date, end_date)
        sp_data_serializer = query_sp_uin(uin, semester)
        # print(sp_data_serializer)
        sp_data_serializer["timelogs"] = saved_data
        sp_data_serializer["current_week"] = get_current_week()
        return Response({"status": "success", "message": message, "data": sp_data_serializer},
                        status=status.HTTP_200_OK)


class TimeLogViewsEmailGet(APIView):
    def get(self, request, email, start_date=None, end_date=None, semester=None):
        message = ""
        if not start_date and not end_date:
            today = datetime.date.today()
            dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
            start_date = dates[0]
            end_date = dates[6]
            message = "retrieval successful for current week"
        elif not end_date:
            end_date = datetime.date.today()
            message = "start date only provided"
        else:
            print(start_date, end_date)
            message = "start date and end date provided"

        saved_data = query_timelog_email(email, start_date, end_date)
        sp_data_serializer = query_sp_email(email, semester)
        sp_data_serializer["timelogs"] = saved_data

        # add current week dates
        sp_data_serializer["current_week"] = get_current_week()
        return Response({"status": "success", "message": message, "data": sp_data_serializer},
                        status=status.HTTP_200_OK)
