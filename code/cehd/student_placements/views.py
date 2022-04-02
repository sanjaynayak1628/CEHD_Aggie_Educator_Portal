import datetime
import json
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from .models import StudentPlacements
from .serializers import StudentPlacementsSerializer


class StudentPlacementsGet(APIView):
    def get(self, request, email, semester=None):
        print("semester: {}, email: {}".format(semester, email))
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
        if len(sp_item_serializer) > 0:
            sp_item_serializer = sp_item_serializer[0]
        else:
            sp_item_serializer = None
        # print(sp_item_serializer)
        # print(type(sp_item_serializer))
        # Output: {} if no value is present, data: {model, pk, fields: {}}
        return Response({"status": "success", "data": sp_item_serializer}, status=status.HTTP_200_OK)
