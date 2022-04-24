import datetime

from rest_framework import serializers
from .models import TimeLogs


def get_date_submitted(obj):
    return datetime.date.today()


class TimeLogsSerializer(serializers.ModelSerializer):
    date_submitted = serializers.SerializerMethodField('get_date_submitted')

    class Meta:
        model = TimeLogs
        db_table = "time_logs"
        fields = ("student_uin", "student_email", "log_date", "notes", "hours_submitted", "hours_approved",
                  "approval_due_date", "semester", "semester_year", "start_time", "end_time", "date_submitted")


class TimeLogsSerializerApprove(serializers.ModelSerializer):
    class Meta:
        model = TimeLogs
        db_table = "time_logs"
        fields = ("student_uin", "student_email", "log_date", "notes", "hours_submitted", "hours_approved",
                  "approval_due_date", "semester", "semester_year", "start_time", "end_time", "date_submitted")
