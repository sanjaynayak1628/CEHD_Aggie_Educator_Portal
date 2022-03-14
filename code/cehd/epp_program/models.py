from django.db import models


class EPPProgram(models.Model):
    """
    EPP Program
    Site-wide app for managing EPP Programs
    """

    program_name = models.CharField(max_length=100)
    """
    Full name of program
    """

    program_abbreviation = models.CharField(max_length=20)
    """
    Abbreviation of program to be used in reports or other locations where the full name is impractical
    """

    program_coordinator = models.CharField(max_length=50, null=True)
    program_email = models.EmailField(max_length=50, null=True)

    initial = models.BooleanField(default=True, help_text='Is this an initial teacher certification?')
    """
    Is this an initial teacher certification?
    """

    route = models.CharField(max_length=30, default='trad')
    """
    TEA defined Route of certification
    """

    has_teaching_fields = models.BooleanField(default=False)
    """
    Does this program have multiple teaching fields?
    """

    admission_notification_text = models.TextField(default='', blank=True,
                                                   help_text='E-mail template for admission offer notification')
    """
    This is the text to be used when sending offer letters for program admission
    """

    auto_assigned_exams = models.TextField(default='', blank=True)
    """
    This will be a JSON string containing each teaching field associated with program and the exams to auto-assign a student at admission.  
    """

    active = models.BooleanField(default=True)
    """
    Can students be admitted to this program or active students in this program?
    """
