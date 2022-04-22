import datetime
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from .models import StudentPlacements
from core.models import Person


def query_student_details(email, uin=None):
    if not email and not uin:
        pass
    person_details = None
    if email:
        person_details = Person.objects.all().filter(primary_email=email)
    elif uin:
        person_details = Person.objects.all().filter(uin=uin)
    if person_details:
        person_details = json.loads(serializers.serialize('json', person_details))
        person_details = person_details[0]["fields"]
        tmp = dict()
        tmp["first_name"] = person_details["first_name"]
        tmp["middle_name"] = person_details["middle_name"]
        tmp["last_name"] = person_details["last_name"]
        tmp["primary_email"] = person_details["primary_email"]
        tmp["secondary_email"] = person_details["secondary_email"]
        if person_details.get("middle_name", "").strip() == "":
            tmp["full_name"] = person_details["first_name"] + " " + person_details["last_name"]
        else:
            tmp["full_name"] = person_details["first_name"] + " " + person_details[
                "middle_name"].strip() + " " + person_details["last_name"]
        person_details = tmp
    return person_details


def query_student_placements_email(email, semester):
    if not semester:
        with open("config.json") as json_config_file:
            config = json.load(json_config_file)
        today_date = datetime.date.today()
        for k, v in config["semester"].items():
            sem_start = today_date.replace(month=v["start_month"], day=v["start_day"])
            sem_end = today_date.replace(month=v["end_month"], day=v["end_day"])
            if sem_start <= today_date <= sem_end:
                semester = k
                break
    sp_items = StudentPlacements.objects.all().filter(student_email=email, semester=semester).distinct("student_email", "semester")
    sp_item_serializer = json.loads(serializers.serialize('json', sp_items))
    return sp_item_serializer


def query_student_placements_uin(uin, semester):
    if not semester:
        with open("config.json") as json_config_file:
            config = json.load(json_config_file)
        today_date = datetime.date.today()
        for k, v in config["semester"].items():
            sem_start = today_date.replace(month=v["start_month"], day=v["start_day"])
            sem_end = today_date.replace(month=v["end_month"], day=v["end_day"])
            if sem_start <= today_date <= sem_end:
                semester = k
                break
    sp_items = StudentPlacements.objects.all().filter(uin=uin, semester=semester).distinct("uin", "semester")
    sp_item_serializer = json.loads(serializers.serialize('json', sp_items))
    return sp_item_serializer


def query_supervisor_email(email, semester):
    if not semester:
        with open("config.json") as json_config_file:
            config = json.load(json_config_file)
        today_date = datetime.date.today()
        for k, v in config["semester"].items():
            sem_start = today_date.replace(month=v["start_month"], day=v["start_day"])
            sem_end = today_date.replace(month=v["end_month"], day=v["end_day"])
            if sem_start <= today_date <= sem_end:
                semester = k
                break
    sp_items = StudentPlacements.objects.all().filter(university_supervisor_email=email, semester=semester)\
        .distinct("university_supervisor_email", "cooperating_teacher_email")
    sp_item_serializer = json.loads(serializers.serialize('json', sp_items))
    return sp_item_serializer


class StudentPlacementsGet(APIView):
    """
    GET
    """
    def get(self, request, email, semester=None):
        sp_item_serializer = query_student_placements_email(email, semester)
        if len(sp_item_serializer) > 0:
            sp_item_serializer = sp_item_serializer[0]
        else:
            sp_item_serializer = None
        return Response({"status": "success", "data": sp_item_serializer}, status=status.HTTP_200_OK)


class SupervisorGet(APIView):
    """
    GET
    """
    def get(self, request, email, semester=None):
        sp_item_serializer = query_supervisor_email(email, semester)
        if len(sp_item_serializer) < 0:
            sp_item_serializer = None
        return Response({"status": "success", "data": sp_item_serializer}, status=status.HTTP_200_OK)
