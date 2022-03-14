from django.db import models
from core.models import Person, MONTH_CHOICES
from epp_program.models import EPPProgram


class EPPStudent(models.Model):
    """
    EPP Student
    Each Certification-seeking student will have one record for each program they are in.  Most would only have program.  But, students
    who also pursue a professional program could have multiple records.
    """
    EXIT_STATUS_CHOICES = [
        ('', ''),
        ('Completed', 'Completed'),
        ('Withdrew', 'Withdrew'),
    ]

    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    program = models.ForeignKey(EPPProgram, on_delete=models.PROTECT)

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    """
    Name is stored here (in addition to name in Person) for student to specify name to be used with TEA for certification.  The name in Person
    would be updated when load Compass data
    """
    cohort = models.CharField(max_length=20, null=True, blank=True)
    """
    cohort is a program-defined grouping as another means to organize students
    """

    teaching_field = models.CharField(max_length=50)
    """
    teaching field associated with program
    """

    teaid = models.IntegerField(null=True, blank=True)
    admission_offer_date = models.DateField(null=True, blank=True)
    admission_acceptance_date = models.DateField(null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)

    admission_overall_gpa = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    admission_last60_gpa = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)
    subject_area_hours = models.IntegerField(null=True, blank=True)
    subject_area_gpa = models.DecimalField(max_digits=4, decimal_places=3, null=True, blank=True)

    #  exit_status = models.CharField( max_length=50, null=True, blank=True, choices=EXIT_STATUS_CHOICES )
    exit_status = models.CharField(max_length=50, null=True, blank=True, default='')
    exit_semester = models.CharField(max_length=5, null=True, blank=True, default='')

    admission_reported_to_tea_date = models.DateField(null=True, blank=True)
    admission_offer_letter = models.TextField(null=True, blank=True)
    admission_acceptance_data = models.TextField(null=True, blank=True)

    """ Previous Degree information needed for Post-Bacc programs (which include Professional programs)"""
    previous_degree = models.CharField(max_length=10, null=True, blank=True)
    previous_degree_institution = models.CharField(max_length=50, null=True, blank=True)
    previous_degree_date_month = models.IntegerField(choices=MONTH_CHOICES, null=True, blank=True)
    previous_degree_date_year = models.IntegerField(null=True, blank=True)

    """ Teaching Certification and years experience required for professional programs """
    teaching_certificate_state = models.CharField(max_length=2, null=True, blank=True)
    teaching_certificate_expiration = models.IntegerField(null=True, blank=True)
    classroom_experience = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    admission_offered_by = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT,
                                             related_name='eppstudent_offered_by_person')
    additional_fields = models.TextField(null=True, blank=True)
    """
    addition_fields will be managed as a JSON string to store other miscelleneous data about this student
    """
    notes = models.TextField(null=True, blank=True)
    """
    notes is a place for the Certification Office to add comments about the student 
    """
