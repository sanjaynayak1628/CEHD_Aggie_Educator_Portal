"""
views file describing the APIs used in coop time sheet API
"""
import json
import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from student_placements.views import get_coop_student_current, query_coop_email, query_student_list_details
from time_logs.views import get_time_logs_generic
from time_logs.serializers import TimeLogsSerializerApprove
from core.models import Person
from time_logs.models import TimeLogs
from utils.emails import timesheet_approve, timesheet_reject
from utils.utility import get_previous_current_week


class CoopStudentCurrent(APIView):
    """
    Get current semester student details of Cooperating View
    """

    def get(self, request, coop_email):
        """
        GET function to get current semester student details of Cooperating View
        """
        student_current_serializer, semester = get_coop_student_current(coop_email)
        student_list = list()
        for student in student_current_serializer["students"]:
            student_list.append(student["primary_email"])
        kwargs = dict()
        kwargs["student_email__in"] = student_list

        # get the previous and current weeks time logs
        prev_cur_dates = get_previous_current_week()
        current = False
        if datetime.date.today().strftime("%Y-%m-%d") > prev_cur_dates["current"]["monday"]:
            current = True
            # get approval due date
            # get next week Monday
            nxt_wk_monday = datetime.datetime.strptime(prev_cur_dates["current"]["sunday"], "%Y-%m-%d").date() + \
                            datetime.timedelta(days=1)
            student_current_serializer["approval_by_date"] = nxt_wk_monday
        else:
            # get approval due date
            student_current_serializer["approval_by_date"] = \
                datetime.datetime.strptime(prev_cur_dates["current"]["monday"], "%Y-%m-%d").date()

        if current:
            kwargs["log_date__gte"] = prev_cur_dates["current"]["monday"]
            kwargs["log_date__lte"] = prev_cur_dates["current"]["sunday"]
            dates_tmp = dict(prev_cur_dates["current"])
        else:
            kwargs["log_date__gte"] = prev_cur_dates["previous"]["monday"]
            kwargs["log_date__lte"] = prev_cur_dates["previous"]["sunday"]
            dates_tmp = dict(prev_cur_dates["previous"])

        time_logs_serializer = get_time_logs_generic(kwargs)
        student_current_serializer["current_week"] = dates_tmp
        date_data = dict()
        hours_approved_check = set()
        for tl in time_logs_serializer:
            date_data[tl["fields"]["log_date"]] = tl["fields"]
            hours_approved_check.add(tl["fields"]["hours_approved"])
        student_current_serializer["timelogs"] = date_data

        print(hours_approved_check)
        approved = True
        if False in hours_approved_check:
            approved = False

        # enable or disable the approve/reject button
        if current:
            student_current_serializer["approve"] = "disabled"
        elif approved:
            student_current_serializer["approve"] = "disabled"
        else:
            student_current_serializer["approve"] = ""
        context = dict()
        context['data'] = student_current_serializer
        # print("Student time serializer")
        # print(student_current_serializer)
        return render(request, f'cooperating/cooperatinginitial.html', status=status.HTTP_200_OK, context=context)


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
    for request_data in request.data.get("data", []):
        idx += 1
        request_data["hours_approved"] = True
        request_data["semester"] = config["reverse_semester"][request_data["semester"].lower()]
        time_log_serializer = TimeLogsSerializerApprove(data=request_data)
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
            # print("Error: ")
            # print(time_log_serializer.errors)
            request_status_fail.append(request_data.get("log_date", None))
    return response_data, request_status_fail


class CoopTimeLogSubmit(APIView):
    """
    Approve/reject the coop time sheets to the DB
    """

    def post(self, request, email, approve):
        """
        POST function to approve/reject the coop time sheets to the DB
        """
        if approve.lower() == "true":
            response_data, request_status_fail = save_time_logs(request)
            response_dict = dict()
            status_mode = status.HTTP_200_OK
            if request_status_fail:
                response_dict["status"] = "error"
                response_dict["message"] = "Time entries for dates: {} are not approved. Please reapprove " \
                                           "again!".format(", ".join(request_status_fail))
                response_dict["data"] = response_data
                status_mode = status.HTTP_400_BAD_REQUEST
            else:
                response_dict["status"] = "success"
                response_dict["message"] = "Time entries approved successfully"
                response_dict["data"] = response_data
                cooperating_teacher_email = request.data.get("cooperating_teacher_email", "")
                cooperating_teacher_name = request.data.get("cooperating_teacher_name", "")
                if cooperating_teacher_email == "":
                    response_dict["status"] = "error"
                    status_mode = status.HTTP_403_FORBIDDEN
                    response_dict["message"] = "Entered time not approved. Co-operating teacher not found."
                # send email notification to student regarding approval of timesheets
                if status_mode == status.HTTP_200_OK:
                    timesheet_approve()
            return Response(response_dict, status=status_mode)
        elif approve.lower() == "false":
            timesheet_reject()
            return Response({"message": "Time entries rejected and notified to the student"}, status=status.HTTP_200_OK)


def query_sp_coop_student(coop_email, semester):
    """
    Helper function to get the list of students under the cooperating teacher
    """
    student_list_serializer, st_list = query_coop_email(coop_email, semester)
    students_dict = dict()
    students_dict["cooperating_teacher_email"] = coop_email
    students_dict["students"] = list()
    students_dict["years"] = list()
    if len(student_list_serializer) > 0:
        years = set()
        for d in student_list_serializer:
            data = d["fields"]
            student = dict()
            if student.get("cooperating_teacher_name", None) is None:
                students_dict["cooperating_teacher_name"] = data["cooperating_teacher"]
            years.add(data["semester_year"])
        years = sorted(years)
        students_dict["years"] = list(years)
    student_details, student_details_list = query_student_list_details(st_list)
    for k, v in student_details.items():
        students_dict["students"].append({"student_full_name": v, "student_email": k})
    return students_dict


class CoopView(APIView):
    """
    Get the list of students under the cooperating teacher
    """

    def get(self, request, coop_email, semester=None):
        """
        GET function implementation to get the list of students under the cooperating teachers
        """

        students_all = query_sp_coop_student(coop_email, semester)
        context = {"status": "success", "message": "data retrieved", "data": students_all}
        return render(request, f'cooperating/cooperatingView.html', context, status=status.HTTP_200_OK)


class CoopViewGet(APIView):
    """
    Get the list of time logs based on conditions
    """

    def get(self, request, coop_email, student_email, semester=None, year=None, start_date=None, end_date=None):
        """
        GET function to get the list of time logs based on the conditions
        """

        # create the data to be consumed by API
        student_coop_all = query_sp_coop_student(coop_email, None)
        student_coop_all["student_email_selected"] = student_email
        st_list = student_coop_all["students"]
        student_list = set()
        for st in st_list:
            student_list.add(st["student_email"])
            if st["student_email"] == student_email:
                student_coop_all["student_full_name_selected"] = st["student_full_name"]
        kwargs = dict()
        kwargs["student_email__in"] = list(student_list)
        if semester:
            with open("config.json") as json_config_file:
                config = json.load(json_config_file)
            kwargs["semester"] = config["reverse_semester"][semester.lower()]
            student_coop_all["semester"] = semester
        if year:
            kwargs["semester_year"] = year
            student_coop_all["semester_year"] = year
        if start_date:
            kwargs["log_date__gte"] = start_date
            student_coop_all["start_date"] = start_date
        if end_date:
            kwargs["log_date__lte"] = end_date
            student_coop_all["end_date"] = end_date
        time_logs_serializer = get_time_logs_generic(kwargs)
        student_coop_all["timelogs"] = list()
        for tl in time_logs_serializer:
            tmp = dict(tl["fields"])
            student_coop_all["timelogs"].append(tmp)
        context = dict()
        context["data"] = student_coop_all
        return render(request, f'cooperating/cooperatingView.html', context=context, status=status.HTTP_200_OK)
