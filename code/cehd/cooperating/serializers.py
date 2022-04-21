import datetime

from rest_framework import serializers
from .models import TimeLogs


class TimeLogsSerializer(serializers.ModelSerializer):
    # student_uin = PersonTimeLogsUin(required=True)
    # student_uin = serializers.SerializerMethodField('get_student_uin')
    date_submitted = serializers.SerializerMethodField('get_date_submitted')

    def get_date_submitted(self, obj):
        return datetime.date.today()

    class Meta:
        model = TimeLogs
        db_table = "time_logs"
        fields = ("student_uin", "student_email", "log_date", "notes", "hours_submitted", "hours_approved", "approval_due_date",
                  "semester", "start_time", "end_time", "date_submitted")