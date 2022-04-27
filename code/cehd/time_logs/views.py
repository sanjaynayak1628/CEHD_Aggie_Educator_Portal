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
from core.models import Person
from student_placements.views import query_student_placements_email, query_student_placements_uin, query_student_details
from .models import TimeLogs
from .serializers import TimeLogsSerializer
from utils.emails import timesheet_submit
from utils.utility import get_current_week


def get_approval_due_date(log_date, i):
    """
    Helper function to retrieve the approval due date - next week Monday
    """

    next_week_date = (datetime.datetime.strptime(log_date, "%Y-%m-%d") + datetime.timedelta(days=7 - i)).strftime(
        "%Y-%m-%d")
    return next_week_date


def save_time_logs(request):
    """
    Helper function for saving or submitting the time logs into DB
    """

    with open("config.json") as json_config_file:
        config = json.load(json_config_file)
    request_status_fail = list()
    response_data = list()
    response_status_list = list()
    idx = -1
    approval_due_date = None
    for request_data in request.data.get("data", []):
        idx += 1
        # change the semester to reverse semester values
        request_data["semester"] = config["reverse_semester"][request_data["semester"].lower()]
        if request_data.get("approval_due_date", None) is None:
            if approval_due_date is None:
                approval_due_date = get_approval_due_date(request_data.get("log_date", None), idx)
        request_data["approval_due_date"] = approval_due_date
        request_data["semester_year"] = request_data["log_date"][:4]
        if request_data.get("hours_approved", None) is None:
            request_data["hours_approved"] = False
        if request_data.get("notes", None) is None:
            request_data["notes"] = ""
        if (request_data.get("hours_submitted", None) is None or request_data.get("hours_submitted",
                                                                                  None).strip() == '') \
                or ((float(request_data.get("hours_submitted", "0").strip())) < 0.0):
            if request_data.get("start_time", None) is not None and request_data.get("end_time", None) is not None:
                timediff = (datetime.datetime.strptime(request_data["end_time"],
                                                       '%Y-%m-%dT%H:%M:%S.%fZ') - datetime.datetime.strptime(
                    request_data["start_time"], '%Y-%m-%dT%H:%M:%S.%fZ')).total_seconds() / 3600
                if round(timediff, 1) < 0:
                    timediff = 0
                request_data["hours_submitted"] = str(round(timediff, 1))
            else:
                request_data["hours_submitted"] = "0"
        request_data["hours_submitted"] = request_data["hours_submitted"].strip()

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
                # print("Exception: {}".format(e))
                request_status_fail.append(request_data.get("log_date", None))
        else:
            # print("Errors")
            # print(time_log_serializer.errors)
            request_status_fail.append(request_data.get("log_date", None))
    return response_data, request_status_fail


class TimeLogViewsSubmit(APIView):
    """
    Submit the time sheets entered by the student
    """

    def post(self, request):
        """
        POST function to submit the time sheets
        """
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
            response_dict["message"] = "Entered time entries submitted successfully"
            response_dict["data"] = response_data
            # send the email to cooperating teacher
            cooperating_teacher_email = request.data.get("cooperating_teacher_email", "")
            cooperating_teacher_name = request.data.get("cooperating_teacher_name", "")
            if cooperating_teacher_email == "":
                response_dict["status"] = "error"
                status_mode = status.HTTP_403_FORBIDDEN
                response_dict["message"] = "Entered time not submitted. Co-operating teacher not found. " \
                                           "Please save the time entries."
            if status_mode == status.HTTP_200_OK:
                student_email_select = request.data.get("student_email_select", "")
                student_name_select = request.data.get("student_name_select", "")
                submission_date = datetime.date.today().strftime("%Y-%m-%d")
                timesheet_submit(student_name_select, student_email_select, submission_date)
        return Response(response_dict, status=status_mode)


class TimeLogViewsSave(APIView):
    """
    Save time sheets to the DB
    """

    def post(self, request):
        """
        POST function implementation to save the time sheets into the DB
        """
        response_data, request_status_fail = save_time_logs(request)
        if request_status_fail:
            return Response({"status": "error",
                             "message": "Time entered for dates: {} are not saved. Please re-save again!".format(
                                 ", ".join(request_status_fail)), "data": response_data},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"status": "success",
             "message": "Entered time entries saved successfully", "student_email_select_email":
                 request.data['student_email_select'], "data": response_data}, status=status.HTTP_200_OK)

    def delete(self, request, student_uin=None, log_date=None):
        """
        DELETE functionality to delete an entry of time log from DB
        """

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
    """
    Helper function to get the data from time logs DB based on UIN
    """

    saved_time = TimeLogs.objects.all().filter(student_uin=uin, log_date__lte=end_date,
                                               log_date__gte=start_date).order_by('log_date')
    saved_time_serializer = json.loads(serializers.serialize('json', saved_time))
    saved_data = dict()
    for sv_data in saved_time_serializer:
        if sv_data.get('fields', None):
            saved_data[sv_data['fields']['log_date']] = sv_data['fields']
    return saved_data


def query_timelog_email(email, start_date, end_date):
    """
    Helper function to get the data from time logs DB based on Email
    """

    saved_time = TimeLogs.objects.all().filter(student_email=email, log_date__lte=end_date,
                                               log_date__gte=start_date).order_by('log_date')
    saved_time_serializer = json.loads(serializers.serialize('json', saved_time))
    saved_data = dict()
    for sv_data in saved_time_serializer:
        if sv_data.get('fields', None):
            saved_data[sv_data['fields']['log_date']] = sv_data['fields']
    return saved_data


def query_sp_email(email, semester=None):
    """
    Helper function to get the data from student placements DB based on Email
    """

    sp_item_serializer = query_student_placements_email(email, semester)
    if len(sp_item_serializer) > 0:
        sp_item_serializer = sp_item_serializer[0]['fields']
        with open("config.json") as json_config_file:
            config = json.load(json_config_file)
        sp_item_serializer["semester"] = config["semester"][sp_item_serializer["semester"]]["name"]
    else:
        sp_item_serializer = dict()
    return sp_item_serializer


def query_sp_uin(uin, semester=None):
    """
    Helper function to get the data from student placements DB based on UIN
    """

    sp_item_serializer = query_student_placements_uin(uin, semester)
    if len(sp_item_serializer) > 0:
        sp_item_serializer = sp_item_serializer[0]['fields']
        with open("config.json") as json_config_file:
            config = json.load(json_config_file)
        sp_item_serializer["semester"] = config["semester"][sp_item_serializer["semester"]]["name"]
    else:
        sp_item_serializer = dict()
    return sp_item_serializer


def get_student_details(email, uin=None):
    """
    Helper function to get the data from Person DB based on email
    """

    person_serializer = query_student_details(email, uin)
    return person_serializer


class TimeLogViewsUinGet(APIView):
    """
    Get the data from time logs DB based on UIN
    """

    def get(self, request, uin, start_date=None, end_date=None, semester=None):
        """
        GET function implementation to get the data from time logs DB based on UIN
        """
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
            message = "start date and end date provided"

        saved_data = query_timelog_uin(uin, start_date, end_date)
        sp_data_serializer = query_sp_uin(uin, semester)
        sp_data_serializer["timelogs"] = saved_data
        sp_data_serializer["current_week"] = get_current_week()
        return Response({"status": "success", "message": message, "data": sp_data_serializer},
                        status=status.HTTP_200_OK)


class TimeLogViewsEmailGet(APIView):
    """
    Get the data from time logs DB based on email
    """

    def get(self, request, email, start_date=None, end_date=None, semester=None, prev=0):
        """
        GET function implementation to get the time logs data based on email
        """
        message = ""
        visit_html = "studentview.html"
        if not start_date and not end_date:
            if prev == 0:
                visit_html = "student.html"
            today = datetime.date.today()
            dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
            start_date = dates[0].strftime("%Y-%m-%d")
            end_date = dates[6].strftime("%Y-%m-%d")
            message = "retrieval successful for current week"
        elif not end_date:
            end_date = datetime.date.today().strftime("%Y-%m-%d")
            message = "start date only provided"
        else:
            message = "start date and end date provided"

        saved_data = query_timelog_email(email, start_date, end_date)
        person_serializer = query_student_details(email)
        sp_data_serializer = query_sp_email(email, semester)
        sp_data_serializer["timelogs"] = saved_data
        sp_data_serializer["student"] = person_serializer
        # add current week dates
        sp_data_serializer["current_week"] = get_current_week()
        sp_data_serializer["start_date"] = start_date
        sp_data_serializer["end_date"] = end_date
        context = {"status": "success", "message": message, "data": sp_data_serializer}
        return render(request, f'time_logs/{visit_html}', context)


def get_time_logs_generic(kwargs):
    time_logs = TimeLogs.objects.all().filter(**kwargs).order_by("log_date")
    time_logs_serializer = json.loads(serializers.serialize('json', time_logs))
    return time_logs_serializer
