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
class StudentViewTest(TestCase):
    """
    This class is for testing the Student View APIs
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
                                         principal="", site="", classroom_type="", semester="sprng",
                                         field_experience_program="", placement="",
                                         beginning_date_experience="2020-01-01", ending_date_experience="2021-01-01",
                                         instructor="")

        TimeLogs.objects.create(student_uin=Person.objects.get(uin=120), student_email="joejonas@xyz.com",
                                log_date="2022-04-07", notes="get test", hours_submitted=10, hours_approved=True,
                                approval_due_date="2022-04-13", semester="sprng", semester_year="2022",
                                start_time="2022-04-07T10:20:10.233-05:30", end_time="2022-04-07T20:20:10.233-05:30",
                                date_submitted="2022-04-06")

        # payload for post - save
        self.invalid_save_payload = {
            "cooperating_teacher_email": "cooperating_teacher@xyz.com",
            "cooperating_teacher_name": "Andrew George",
            "email": "joejonas@xyz.com",
            "student_email_select": "joejonas@xyz.com",
            "data": [{
                "student_uin": "10",
                "student_email": "joejonas@xyz.com",
                "log_date": "2020-04-04",
                "notes": "submit entry",
                "hours_submitted": "10",
                "hours_approved": False,
                "semester": "spring",
                "semester_year": "2022",
                "start_time": "2022-04-03T10:20:10.233-05:30",
                "end_time": "2022-04-03T12:20:10.233-05:30"
            }]
        }

        # payload for post - submit
        self.valid_submit_save_payload = {
            "cooperating_teacher_email": "cooperating_teacher@xyz.com",
            "cooperating_teacher_name": "Andrew George",
            "email": "joejonas@xyz.com",
            "student_email_select": "joejonas@xyz.com",
            "data": [{
                "student_uin": "120",
                "student_email": "joejonas@xyz.com",
                "log_date": "2020-04-07",
                "notes": "submit entry",
                "hours_submitted": "10",
                "hours_approved": False,
                "semester": "spring",
                "semester_year": "2022",
                "start_time": "2022-04-07T12:20:10.233-04:30",
                "end_time": "2022-04-07T20:20:10.233-04:30"
            }]
        }

        self.invalid_submit_payload = {
            "cooperating_teacher_email": "",
            "cooperating_teacher_name": "Andrew George",
            "email": "joejonas@xyz.com",
            "student_email_select": "joejonas@xyz.com",
            "data": [{
                "student_uin": "120",
                "student_email": "joejonas@xyz.com",
                "log_date": "2020-04-07",
                "notes": "submit entry",
                "hours_submitted": "10",
                "hours_approved": False,
                "semester": "spring",
                "semester_year": "2022",
                "start_time": "2022-04-07T12:20:10.233-04:30",
                "end_time": "2022-04-07T20:20:10.233-04:30"
            }]
        }

        self.valid_submit_payload_without_name = {
            "cooperating_teacher_email": "cooperating_teacher@xyz.com",
            "cooperating_teacher_name": "",
            "email": "joejonas@xyz.com",
            "student_email_select": "joejonas@xyz.com",
            "data": [{
                "student_uin": "120",
                "student_email": "joejonas@xyz.com",
                "log_date": "2020-04-07",
                "notes": "submit entry",
                "hours_submitted": "10",
                "hours_approved": False,
                "semester": "spring",
                "semester_year": "2022",
                "start_time": "2022-04-07T12:20:10.233-04:30",
                "end_time": "2022-04-07T20:20:10.233-04:30"
            }]
        }

    def test_valid_submit(self):
        """
        This function is used to check the correctness of Student View POST APIs - submit
        return: 200 Correct Response
        """
        response = client.post(reverse('student_submit_time_logs', kwargs={"email": "joejonas@xyz.com"}),
                               data=json.dumps(self.valid_submit_save_payload), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_submit_without_name(self):
        """
        This function is used to check the correctness of Student View POST APIs - submit
        return: 200 Correct Response
        """
        response = client.post(reverse('student_submit_time_logs', kwargs={"email": "joejonas@xyz.com"}),
                               data=json.dumps(self.valid_submit_payload_without_name), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_submit(self):
        """
        This function is used to check the correctness of Student View POST APIs - submit
        return: 400 Error Response
        """
        response = client.post(reverse('student_submit_time_logs', kwargs={"email": "joejonas@xyz.com"}),
                               data=json.dumps(self.invalid_submit_payload), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_invalid_submit_data(self):
        """
        This function is used to check the correctness of Student View POST APIs - submit
        return: 400 Error Response
        """
        response = client.post(reverse('student_submit_time_logs', kwargs={"email": "joejonas@xyz.com"}),
                               data=json.dumps(self.invalid_save_payload), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_save(self):
        """
        This function is used to check the correctness of Student View POST APIs - save
        return: 200 Correct Response
        """
        response = client.post(reverse('student_save_time_logs', kwargs={"email": "joejonas@xyz.com"}),
                               data=json.dumps(self.valid_submit_save_payload), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_save(self):
        """
        This function is used to check the correctness of Student View POST APIs - save
        return: 400 Error Response
        """
        response = client.post(reverse('student_save_time_logs', kwargs={"email": "joejonas@xyz.com"}),
                               data=json.dumps(self.invalid_save_payload), content_type="application/json")
        response_dict = response.json()
        self.assertEqual(response_dict.get("message", ""),
                         "Time entered for dates: 2020-04-04 are not saved. Please re-save again!")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_uin_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_uin_get_time_logs", kwargs={"uin": 120}))
        # self.assertEqual(response.json().get("message", "No message"), "retrieval successful for current week")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_uin_sem_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_uin_sem_get_time_logs", kwargs={"uin": 120, "semester": "spring"}))
        # self.assertEqual(response.json().get("message", "No message"), "retrieval successful for current week")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_uin_start_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_uin_start_get_time_logs", kwargs={"uin": 120, "start_date": "2022-04-01"}))
        # self.assertEqual(response.json().get("message", "No message"), "start date only provided")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_uin_start_end_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_uin_startend_get_time_logs",
                                      kwargs={"uin": 120, "start_date": "2022-04-01", "end_date": "2022-04-05"}))
        # self.assertEqual(response.json().get("message", "No message"), "start date and end date provided")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_email_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_email_get_time_logs", kwargs={"email": "joejonas@xyz.com"}))
        # self.assertEqual(response.json().get("message", "No message"), "retrieval successful for current week")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_email_sem_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_email_sem_get_time_logs",
                                      kwargs={"email": "joejonas@xyz.com", "semester": "spring"}))
        # self.assertEqual(response.json().get("message", "No message"), "retrieval successful for current week")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_email_start_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_email_start_get_time_logs",
                                      kwargs={"email": "joejonas@xyz.com", "start_date": "2022-04-01"}))
        # self.assertEqual(response.json().get("message", "No message"), "start date only provided")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_email_start_end_get(self):
        """
        This function is used to check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.get(reverse("student_email_startend_get_time_logs",
                                      kwargs={"email": "joejonas@xyz.com", "start_date": "2022-04-01",
                                              "end_date": "2022-04-05"}))
        # self.assertEqual(response.json().get("message", "No message"), "start date and end date provided")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_valid_delete(self):
        """
        This function is used the check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.delete(reverse("student_delete_time_logs",
                                         kwargs={"student_uin": 120, "log_date": "2022-04-07"}))
        self.assertEqual(response.json().get("message", "no message"), "Delete successful")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete(self):
        """
        This function is used the check the correctness of Student View GET APIs
        return: 200 Correct Response
        """
        response = client.delete(reverse("student_delete_time_logs",
                                         kwargs={"student_uin": 120, "log_date": "2022-04-08"}))
        self.assertEqual(response.json().get("message", "no message"), "Delete unsuccessful")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
