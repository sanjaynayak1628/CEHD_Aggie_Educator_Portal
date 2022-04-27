import csv
import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from student_placements.views import query_supervisor_email, get_student_super_coop, get_super_coop_details, \
    query_student_list_details
from time_logs.views import get_time_logs_generic


def query_sp_supervisor_coop(super_email, semester):
    """
    Helper function to get the list of cooperating teachers under the supervisor
    """
    sp_item_serializer = query_supervisor_email(super_email, semester)
    coop_dict = dict()
    coop_dict["university_supervisor_email"] = super_email
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
        coop_dict[super_email] = list()
    return coop_dict


class SupervisorCoopView(APIView):
    """
    Get the list of cooperating teachers under the supervisor
    """

    def get(self, request, super_email, semester=None):
        """
        GET function implementation to get the list of cooperating teachers under the supervisor
        """

        coop_all = query_sp_supervisor_coop(super_email, semester)
        context = {"status": "success", "message": "data retrieved", "data": coop_all}
        return render(request, f'supervisor/supervisorView.html', context, status=status.HTTP_200_OK)


class SupervisorCoopGet(APIView):
    """
    Get the time logs for each student against selected cooperating teacher under the supervisor
    """

    def get(self, request, super_email, coop_email, semester=None, year=None, start_date=None, end_date=None,
            export=None):
        """
        GET function to get the time logs for each student against selected cooperating teacher under the supervisor
        """

        # create the data to be consumed by frontend
        super_coop_data = dict()
        super_coop_data["university_supervisor_email"] = super_email
        super_coop_data["cooperating_teacher_email"] = coop_email
        super_coop_data["cooperating_teachers"] = list()
        super_coop_data["years"] = list()
        sp_item_serializer = query_supervisor_email(super_email, None)
        if len(sp_item_serializer) > 0:
            years = set()
            for d in sp_item_serializer:
                data = d["fields"]
                coop = dict()
                if coop.get("university_supervisor_name", None) is None:
                    super_coop_data["university_supervisor_name"] = data["university_supervisor"]
                coop["cooperating_teacher"] = data["cooperating_teacher"]
                coop["cooperating_teacher_email"] = data["cooperating_teacher_email"]
                if data["cooperating_teacher_email"] == coop_email:
                    super_coop_data["cooperating_teacher_selected"] = data["cooperating_teacher"]
                    super_coop_data["cooperating_teacher_email_selected"] = data["cooperating_teacher_email"]
                super_coop_data["cooperating_teachers"].append(coop)
                years.add(data["semester_year"])
            years = sorted(years)
            super_coop_data["years"] = list(years)

        kwargs = dict()
        student_list = get_student_super_coop(super_email, coop_email)
        student_names, student_names_list = query_student_list_details(student_list)
        kwargs["student_email__in"] = student_list
        if semester:
            with open("config.json") as json_config_file:
                config = json.load(json_config_file)
            kwargs["semester"] = config["reverse_semester"][semester.lower()]
            super_coop_data["semester"] = semester
        if year:
            kwargs["semester_year"] = year
            super_coop_data["semester_year"] = year
        if start_date:
            kwargs["log_date__gte"] = start_date
            super_coop_data["start_date"] = start_date
        if end_date:
            kwargs["log_date__lte"] = end_date
            super_coop_data["end_date"] = end_date
        time_logs_serializer = get_time_logs_generic(kwargs)

        super_coop_data["timelogs"] = list()
        for tl in time_logs_serializer:
            tmp = dict(tl["fields"])
            tmp["student_name"] = student_names[tl["fields"]["student_email"]]
            super_coop_data["timelogs"].append(tmp)

        if export == "true":
            response = HttpResponse(content_type="text/csv")
            csv_keys = ["student name", "student email", "cooperating teacher", "cooperating teacher email",
                        "log date", "notes", "hours submitted", "hours approved", "approval due date", "semester",
                        "semester year", "start time", "end time", "date submitted"]
            writer = csv.writer(response)
            writer.writerow(csv_keys)
            for tl in super_coop_data["timelogs"]:
                # list of data
                # append data to the list in the same order as the csv keys
                tmp = list()
                tmp.append(tl["student_name"])
                tmp.append(tl["student_email"])
                tmp.append(super_coop_data["cooperating_teacher_selected"])
                tmp.append(super_coop_data["cooperating_teacher_email"])
                tmp.append(tl["log_date"])
                tmp.append(tl["notes"])
                tmp.append(tl["hours_submitted"])
                tmp.append(tl["hours_approved"])
                tmp.append(tl["approval_due_date"])
                tmp.append(tl["semester"])
                tmp.append(tl["semester_year"])
                tmp.append(tl["start_time"])
                tmp.append(tl["end_time"])
                tmp.append(tl["date_submitted"])
                writer.writerow(tmp)

            response["Content-Disposition"] = 'attachment; filename=supervisor_data.csv'
            return response

        context = {"status": "success", "message": "data retrieved", "data": super_coop_data}
        return render(request, f'supervisor/supervisorView.html', context, status=status.HTTP_200_OK)
