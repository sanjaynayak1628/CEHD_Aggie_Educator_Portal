from django.db import models
from epp_student.models import EPPStudent


class StudentPlacements(models.Model):
    """
    This is the model for student placements table that is connected with time logs table
    """
    eppstudent = models.ForeignKey(EPPStudent, on_delete=models.PROTECT)
    university_supervisor_email = models.EmailField()
    university_supervisor = models.CharField(max_length=100)
    cooperating_teacher_email = models.EmailField()
    cooperating_teacher = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    site = models.CharField(max_length=50)
    classroom_type = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    field_experience_program = models.CharField(max_length=50)
    placement = models.CharField(max_length=50)
    beginning_date_experience = models.DateField()
    ending_date_experience = models.DateField()
    instructor = models.CharField(max_length=50)
