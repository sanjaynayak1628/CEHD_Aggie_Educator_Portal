from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


MONTH_CHOICES = (
  ('', ''),
  (1, 'Jan'),
  (2, 'Feb'),
  (3, 'Mar'),
  (4, 'Apr'),
  (5, 'May'),
  (6, 'Jun'),
  (7, 'Jul'),
  (8, 'Aug'),
  (9, 'Sep'),
  (10, 'Oct'),
  (11, 'Nov'),
  (12, 'Dec'),
)


class Person(AbstractBaseUser):
    """
    Base User Model
    """

    CAMPUS_OPTIONS = (
        ('CS', 'College Station'),
        ('GA', 'Galveston'),
        ('XX', 'Other')
    )
    GENERATION_OPTIONS = (
        ('SR', 'Sr.'),
        ('JR', 'Jr.'),
        ('III', 'III'),
    )

    ETHNICITY_OPTIONS = (
        ('A', 'Asian'),
        ('B', 'Black'),
        ('H', 'Hispanic'),
        ('I', 'I'),
        ('M', 'M'),
        ('N', 'N'),
        ('O', 'O'),
        ('T', 'T'),
        ('W', 'White'),
        ('X', 'Unknown'),
    )

    SEX_OPTIONS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('X', 'Unknown')
    )

    person_id = models.AutoField(primary_key=True)
    """
    uin is the username so should be present and unique.
    For non-tamu people, must define a CEHD-version of an uin.  These values will be a 9 digit number
    but with the middle pair of numbers being 11 instead of 00.
    """
    uin = models.PositiveIntegerField(blank=True, default=0, unique=True, db_index=True)
    netid = models.CharField(max_length=50, blank=True)
    campus = models.CharField(max_length=2, choices=CAMPUS_OPTIONS, default='CS')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    use_middle_name = models.BooleanField(default=False)
    generation = models.CharField(max_length=3, choices=GENERATION_OPTIONS, blank=True, default='')
    primary_email = models.EmailField(blank=True)  # This should be @tamu.edu if available
    secondary_email = models.EmailField(blank=True)
    primary_ethnicity = models.CharField(max_length=1, choices=ETHNICITY_OPTIONS, default='X')
    latino = models.BooleanField(default=False)
    country_of_origin = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS, default='X')
    birth_date = models.DateField(null=True, blank=True)
    notes = models.TextField(max_length=5000, blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('self', null=True, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login_ip = models.CharField(max_length=50, null=True)
