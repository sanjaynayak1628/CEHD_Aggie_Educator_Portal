from rest_framework import serializers
from .models import TimeLogs


class TimeLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLogs
        fields = ["eppstudent", "log_date", "notes", "hours_submitted", "hours_approved", "approval_due_date",
                  "semester", "start_time", "end_time"]