from django.db import models
from student_placements.models import StudentPlacements


class TimeLogs(models.Model):
    """
    This is the model for time logs
    """
    eppstudent = models.ForeignKey(StudentPlacements, on_delete=models.PROTECT)
    log_date = models.DateField()
    notes = models.TextField(default="")
    hours_submitted = models.PositiveIntegerField(default=0)
    hours_approved = models.BooleanField()
    approval_due_date = models.DateField()
    semester = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_submitted = models.DateField(auto_now=True)
