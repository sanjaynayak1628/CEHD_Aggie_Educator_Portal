from django.db import models


class Authentication(models.Model):
    """
    This is the model for authentication to the database for login purpose
    """
    """
    uin is the username so should be present and unique.
    For non-tamu people, must define a CEHD-version of an uin.  These values will be a 9 digit number
    but with the middle pair of numbers being 11 instead of 00.
    """
    uin = models.PositiveIntegerField(blank=True, default=0, unique=True, db_index=True)
    netid = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=10, blank=False)
