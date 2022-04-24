"""
views file describing the APIs used in coop time sheet API
"""
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from student_placements.views import get_coop_student_current
from time_logs.views import get_time_logs_generic
from time_logs.serializers import TimeLogsSerializer
from core.models import Person
from time_logs.models import TimeLogs
from utils.emails import timesheet_approve


class CoopViews(APIView):
    """
    GET function to view the coop time sheets from the DB
    """

    def get(self, request, email, start_date=None, end_date=None, semester=None, approved=None, year=None):
        """
        GET function implementation
        """
        return render(request, f'cooperating/cooperatingview.html', status=status.HTTP_200_OK)


class CoopStudentCurrent(APIView):
    """
    GET function to get current semester student details of Cooperating View
    """

    def get(self, request, coop_email):
        student_current_serializer, semester = get_coop_student_current(coop_email)
        semester_year = student_current_serializer["semester_year"]
        student_list = list()
        for student in student_current_serializer["students"]:
            student_list.append(student["primary_email"])
        kwargs = dict()
        kwargs["student_email__in"] = student_list
        kwargs["semester"] = semester
        kwargs["semester_year"] = semester_year
        time_logs_serializer = get_time_logs_generic(kwargs)
        student_current_serializer["timelogs"] = list()
        for tl in time_logs_serializer:
            student_current_serializer["timelogs"].append(tl["fields"])

        # enable or disable the approve/reject button
        student_current_serializer["approve"] = "true"
        print(student_current_serializer)
        context = dict()
        context['data'] = student_current_serializer
        return render(request, f'cooperating/cooperatinginitial.html', status=status.HTTP_200_OK, context=context)


def save_time_logs(request):
    """
    Helper function for saving or submitting the time logs into DB
    """

    request_status_fail = list()
    response_data = list()
    response_status_list = list()
    idx = -1
    for request_data in request.data.get("data", []):
        idx += 1
        request_data["hours_approved"] = True
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
            # print(time_log_serializer.errors)
            request_status_fail.append(request_data.get("log_date", None))
    return response_data, request_status_fail


class CoopTimeLogSubmit(APIView):
    """
    POST function to approve/reject the coop time sheets to the DB
    """

    def post(self, request):
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
