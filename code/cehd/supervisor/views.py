import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from student_placements.views import query_supervisor_email, get_student_super_coop
from time_logs.views import get_time_logs_supervisor


def query_sp_supervisor_coop(email, semester):
    sp_item_serializer = query_supervisor_email(email, semester)
    coop_dict = dict()
    coop_dict["university_supervisor_email"] = email
    coop_dict["cooperating_teachers"] = list()
    coop_dict["years"] = list()
    if len(sp_item_serializer) > 0:
        years = set()
        for d in sp_item_serializer:
            data = d["fields"]
            coop = dict()
            with open("config.json") as json_config_file:
                config = json.load(json_config_file)
            if coop.get("university_supervisor_name", None) is None:
                coop_dict["university_supervisor_name"] = data["university_supervisor"]
            coop["cooperating_teacher"] = data["cooperating_teacher"]
            coop["cooperating_teacher_email"] = data["cooperating_teacher_email"]
            coop_dict["cooperating_teachers"].append(coop)
            years.add(data["semester_year"])
        years = sorted(years)
        coop_dict["years"] = list(years)
    else:
        coop_dict[email] = list()
    return coop_dict


class SupervisorCoopView(APIView):
    """
    Get function to view the time sheets with co op and student view
    """
    def get(self, request, email, semester=None):
        """
        GET function implementation
        """

        coop_all = query_sp_supervisor_coop(email, semester)
        print(coop_all)
        context = {"status": "success", "message": "data retrieved", "data": coop_all}
        return render(request, f'supervisor/supervisorView.html', context, status=status.HTTP_200_OK)


class SupervisorGet(APIView):
    """
    Class to get the time logs for each selected cooperating teacher under the supervisor
    """
    def get(self, request, super_email, coop_email, semester=None, year=None, start_date=None, end_date=None):
        context = {"status": "success", "message": ""}
        if semester is None and year is None and start_date is None and end_date is None:
            message = "Please enter valid filters!"
            context["message"] = message
            context["data"] = list()
            return render(request, f'supervisor/supervisorView.html', context)
        kwargs = dict()
        student_list = get_student_super_coop(super_email, coop_email)
        kwargs["student_email__in"] = student_list
        if semester:
            with open("config.json") as json_config_file:
                config = json.load(json_config_file)
            kwargs["semester"] = config["reverse_semester"][semester]
        if year:
            kwargs["semester_year"] = year
        if start_date:
            kwargs["{}__gte".format(start_date)] = start_date
        if end_date:
            kwargs["{}__lte".format(end_date)] = end_date
        time_logs_serializer = get_time_logs_supervisor(kwargs)
        print(time_logs_serializer)
        context = {"status": "success", "message": "data retrieved", "data": time_logs_serializer}
        return render(request, f'supervisor/supervisorView.html', context, status=status.HTTP_200_OK)
