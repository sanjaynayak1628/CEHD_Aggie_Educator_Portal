import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from core.models import Person


class TimeLogs(models.Model):
    """
    This is the model for time logs
    """
    student_uin = models.ForeignKey(Person, on_delete=models.PROTECT, to_field='uin', related_name="person_uin", default=0)
    student_email = models.EmailField()
    log_date = models.DateField()
    notes = models.TextField(default="", blank=True)
    hours_submitted = models.PositiveIntegerField(default=0)
    hours_approved = models.BooleanField()
    approval_due_date = models.DateField()
    semester = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_submitted = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "time_logs"
        # don't use unique_together if using update_or_create in time_logs/views.py
        # unique_together = (('student_uin', 'log_date'),)
