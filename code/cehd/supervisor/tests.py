import datetime
import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from core.models import Person
from epp_program.models import EPPProgram
from epp_student.models import EPPStudent
from student_placements.models import StudentPlacements
from time_logs.models import TimeLogs

client = Client()


# noinspection DuplicatedCode
class SupervisorTest(TestCase):
    """
    This class is for testing the Supervisor APIs
    """

    def setUp(self):
        # create Person objects
        Person.objects.create(person_id=120, uin=120, netid="joejonas", campus="CS", first_name="Joe", middle_name="",
                              last_name="Jonas", use_middle_name=False, generation="", primary_email="joejonas@xyz.com",
                              secondary_email="joejonassec@xyz.com", primary_ethnicity="X", latino=False,
                              country_of_origin="", sex="M", birth_date="1990-02-12", notes="",
                              last_updated_at=datetime.datetime.now(), last_updated_by=None, is_active=True,
                              is_admin=False, is_superuser=False, last_login_ip="10.0.0.21")

        Person.objects.create(person_id=100, uin=100, netid="emilyblake", campus="CS", first_name="Emily",
                              middle_name="", last_name="Blake", use_middle_name=False, generation="",
                              primary_email="emily@xyz.com", secondary_email="blake@xyz.com", primary_ethnicity="X",
                              latino=False, country_of_origin="", sex="F", birth_date="1985-02-12", notes="",
                              last_updated_at=datetime.datetime.now(),
                              last_updated_by=None, is_active=True, is_admin=False, is_superuser=False,
                              last_login_ip="10.0.0.21")

        Person.objects.create(person_id=99, uin=99, netid="clarkkent", campus="CS", first_name="Clark", middle_name="",
                              last_name="Kent",
                              use_middle_name=False, generation="", primary_email="clark@xyz.com",
                              secondary_email="kent@xyz.com", primary_ethnicity="X", latino=False,
                              country_of_origin="", sex="M", birth_date="1985-10-12", notes="",
                              last_updated_at=datetime.datetime.now(),
                              last_updated_by=None, is_active=True, is_admin=False, is_superuser=False,
                              last_login_ip="10.0.0.21")

        EPPProgram.objects.create(program_name="management course", program_abbreviation="mgmt", program_coordinator="",
                                  program_email="", initial=True, route="trad", has_teaching_fields=False,
                                  admission_notification_text="", auto_assigned_exams="", active=True)

        EPPStudent.objects.create(person=Person.objects.get(person_id=120), program=EPPProgram.objects
                                  .get(program_name="management course"), first_name="Joe", middle_name="",
                                  last_name="Jonas", cohort="", teaching_field="", teaid=1,
                                  admission_offer_date="2020-04-03", admission_acceptance_date="2020-04-13",
                                  admission_date="2020-05-03", admission_overall_gpa=4.0, admission_last60_gpa=4.0,
                                  subject_area_hours=20, subject_area_gpa=4.0, exit_status="", exit_semester="sprng",
                                  admission_reported_to_tea_date="2020-04-30", admission_offer_letter="",
                                  admission_acceptance_data="2020-04-13", previous_degree="B.S.",
                                  previous_degree_institution="Texas A&M University", previous_degree_date_month=5,
                                  previous_degree_date_year=2019, teaching_certificate_state="",
                                  teaching_certificate_expiration=1, classroom_experience=1.2,
                                  admission_offered_by=Person.objects.get(person_id=100), additional_fields="",
                                  notes="")

        StudentPlacements.objects.create(eppstudent=EPPStudent.objects.get(person_id=120), uin=Person.objects
                                         .get(person_id=120), student_email="joejonas@xyz.com",
                                         university_supervisor_email="emily@xyz.com",
                                         university_supervisor="Emily Blake",
                                         cooperating_teacher_email="clark@xyz.com", cooperating_teacher="Clark Kent",
                                         principal="", site="", classroom_type="", semester="spring",
                                         field_experience_program="", placement="",
                                         beginning_date_experience="2020-01-01", ending_date_experience="2021-01-01",
                                         instructor="")

        TimeLogs.objects.create(student_uin=Person.objects.get(uin=120), student_email="joejonas@xyz.com",
                                log_date="2022-04-07", notes="get test", hours_submitted=10, hours_approved=True,
                                approval_due_date="2022-04-13", semester="sprng", semester_year="2022",
                                start_time="2022-04-07T10:20:10.233-05:30", end_time="2022-04-07T20:20:10.233-05:30",
                                date_submitted="2022-04-06")

    def test_supervisor_home(self):
        """
        This function is used to check the correctness of Supervisor home page
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_view", kwargs={"super_email": "emily@xyz.com"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop", kwargs={"super_email": "emily@xyz.com",
                                                                 "coop_email": "clark@xyz.com"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_semester(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher and email
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem", kwargs={"super_email": "emily@xyz.com",
                                                                     "coop_email": "clark@xyz.com",
                                                                     "semester": "spring"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_semester_year(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem_year", kwargs={"super_email": "emily@xyz.com",
                                                                          "coop_email": "clark@xyz.com",
                                                                          "semester": "spring",
                                                                          "year": "2022"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_year(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_year", kwargs={"super_email": "emily@xyz.com",
                                                                      "coop_email": "clark@xyz.com",
                                                                      "year": "2022"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_dates(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_dates", kwargs={"super_email": "emily@xyz.com",
                                                                       "coop_email": "clark@xyz.com",
                                                                       "start_date": "2022-04-18",
                                                                       "end_date": "2022-04-25"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_sem_dates_year(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem_dates_year", kwargs={"super_email": "emily@xyz.com",
                                                                                "coop_email": "clark@xyz.com",
                                                                                "semester": "spring",
                                                                                "year": "2022",
                                                                                "start_date": "2022-04-18",
                                                                                "end_date": "2022-04-25"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_sem_dates(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem_dates", kwargs={"super_email": "emily@xyz.com",
                                                                           "coop_email": "clark@xyz.com",
                                                                           "semester": "spring",
                                                                           "start_date": "2022-04-18",
                                                                           "end_date": "2022-04-25"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_year_dates(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher
        return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_year_dates", kwargs={"super_email": "emily@xyz.com",
                                                                            "coop_email": "clark@xyz.com",
                                                                            "year": "2022",
                                                                            "start_date": "2022-04-18",
                                                                            "end_date": "2022-04-25"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher for export
        functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_export", kwargs={"super_email": "emily@xyz.com",
                                                                        "coop_email": "clark@xyz.com",
                                                                        "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_semester_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher and email
        for export functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem_export", kwargs={"super_email": "emily@xyz.com",
                                                                            "coop_email": "clark@xyz.com",
                                                                            "semester": "spring", "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_semester_year_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher for export
        functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem_year_export", kwargs={"super_email": "emily@xyz.com",
                                                                                 "coop_email": "clark@xyz.com",
                                                                                 "semester": "spring",
                                                                                 "year": "2022", "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_year_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher for export
        functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_year_export", kwargs={"super_email": "emily@xyz.com",
                                                                             "coop_email": "clark@xyz.com",
                                                                             "year": "2022", "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_dates_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher for export
        functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_dates_export", kwargs={"super_email": "emily@xyz.com",
                                                                              "coop_email": "clark@xyz.com",
                                                                              "start_date": "2022-04-18",
                                                                              "end_date": "2022-04-25",
                                                                              "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_sem_dates_year_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher for export
        functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem_dates_year_export", kwargs={"super_email": "emily@xyz.com",
                                                                                       "coop_email": "clark@xyz.com",
                                                                                       "semester": "spring",
                                                                                       "year": "2022",
                                                                                       "start_date": "2022-04-18",
                                                                                       "end_date": "2022-04-25",
                                                                                       "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_sem_dates_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher for export
        functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_sem_dates_export", kwargs={"super_email": "emily@xyz.com",
                                                                                  "coop_email": "clark@xyz.com",
                                                                                  "semester": "spring",
                                                                                  "start_date": "2022-04-18",
                                                                                  "end_date": "2022-04-25",
                                                                                  "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supervisor_coop_year_dates_export(self):
        """
        This function is used to check the correctness of Supervisor API with selected cooperating teacher for export
        functionality return: 200 Correct Response
        """
        response = client.get(reverse("supervisor_coop_year_dates_export", kwargs={"super_email": "emily@xyz.com",
                                                                                   "coop_email": "clark@xyz.com",
                                                                                   "year": "2022",
                                                                                   "start_date": "2022-04-18",
                                                                                   "end_date": "2022-04-25",
                                                                                   "export": "true"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
