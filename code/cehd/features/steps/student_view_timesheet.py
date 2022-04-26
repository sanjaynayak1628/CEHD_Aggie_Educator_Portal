import time

from behave import *
from test.factories.user import UserFactory
import factory
from selenium.webdriver.support.ui import Select
from utils.utility import get_current_week
from core.models import Person
from epp_program.models import EPPProgram
from epp_student.models import EPPStudent
from student_placements.models import StudentPlacements
from time_logs.models import TimeLogs

use_step_matcher("re")


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person
        django_get_or_create = ("person_id", "uin", "netid", "campus", "first_name", "middle_name", "last_name",
                                "use_middle_name", "generation", "primary_email", "secondary_email",
                                "primary_ethnicity", "latino", "country_of_origin", "sex", "birth_date", "notes",
                                "last_updated_at", "last_updated_by", "is_active", "is_admin", "is_superuser",
                                "last_login_ip")


class EPPProgramFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EPPProgram
        django_get_or_create = ("program_name", "program_abbreviation", "program_coordinator",
                                "program_email", "initial", "route", "has_teaching_fields",
                                "admission_notification_text", "auto_assigned_exams", "active")


class EPPStudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EPPStudent
        django_get_or_create = ("person", "program", "first_name", "middle_name", "last_name", "cohort",
                                "teaching_field", "admission_offer_date", "admission_acceptance_date",
                                "admission_date", "admission_overall_gpa", "admission_last60_gpa",
                                "subject_area_hours", "subject_area_gpa", "exit_status", "exit_semester",
                                "admission_reported_to_tea_date", "admission_offer_letter",
                                "admission_acceptance_data", "previous_degree", "previous_degree_institution",
                                "previous_degree_date_month", "previous_degree_date_year", "teaching_certificate_state",
                                "teaching_certificate_expiration", "classroom_experience", "admission_offered_by",
                                "additional_fields", "notes")


class StudentPlacementsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StudentPlacements
        django_get_or_create = ("eppstudent", "uin", "student_email", "university_supervisor_email",
                                "university_supervisor", "cooperating_teacher_email", "cooperating_teacher",
                                "principal", "site", "classroom_type", "semester", "field_experience_program",
                                "placement", "beginning_date_experience", "ending_date_experience", "instructor")


class TimeLogsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TimeLogs
        django_get_or_create = ("student_uin", "student_email", "log_date", "notes", "hours_submitted",
                                "hours_approved", "approval_due_date", "semester", "semester_year", "start_time",
                                "end_time", "date_submitted")


@given("I am a registered student to view")
def step_impl(context):
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='joejonas@xyz.com', email='joejonas@xyz.com')
    u.set_password('Password123*')
    # Don't omit to call save() to insert object in database
    u.save()

    person1 = PersonFactory(person_id=120, uin=120, netid="joejonas", campus="CS", first_name="Joe", middle_name="",
                            last_name="Jonas", use_middle_name=False, generation="", primary_email="joejonas@xyz.com",
                            secondary_email="joejonassec@xyz.com", primary_ethnicity="X", latino=False,
                            country_of_origin="", sex="M", birth_date="1990-02-12", notes="",
                            last_updated_at="2022-04-03T10:20:10.233-05:30", last_updated_by=None, is_active=True,
                            is_admin=False, is_superuser=False, last_login_ip="10.0.0.21")
    person2 = PersonFactory(person_id=100, uin=100, netid="emilyblake", campus="CS", first_name="Emily",
                            middle_name="", last_name="Blake", use_middle_name=False, generation="",
                            primary_email="emily@xyz.com", secondary_email="blake@xyz.com", primary_ethnicity="X",
                            latino=False, country_of_origin="", sex="F", birth_date="1985-02-12", notes="",
                            last_updated_at="2022-04-03T10:20:10.233-05:30",
                            last_updated_by=None, is_active=True, is_admin=False, is_superuser=False,
                            last_login_ip="10.0.0.21")
    person1.save()
    person2.save()

    eppprogram = EPPProgramFactory(program_name="management course", program_abbreviation="mgmt",
                                   program_coordinator="",
                                   program_email="", initial=True, route="trad", has_teaching_fields=False,
                                   admission_notification_text="", auto_assigned_exams="", active=True)
    eppprogram.save()

    eppstudent = EPPStudentFactory(person=person1, program=eppprogram,
                                   first_name="Joe", middle_name="", last_name="Jonas", cohort="", teaching_field="",
                                   teaid=1, admission_offer_date="2020-04-03", admission_acceptance_date="2020-04-13",
                                   admission_date="2020-05-03", admission_overall_gpa=4.0, admission_last60_gpa=4.0,
                                   subject_area_hours=20, subject_area_gpa=4.0, exit_status="", exit_semester="sprng",
                                   admission_reported_to_tea_date="2020-04-30", admission_offer_letter="",
                                   admission_acceptance_data="2020-04-13", previous_degree="B.S.",
                                   previous_degree_institution="Texas A&M University", previous_degree_date_month=5,
                                   previous_degree_date_year=2019, teaching_certificate_state="",
                                   teaching_certificate_expiration=1, classroom_experience=1.2,
                                   admission_offered_by=person2, additional_fields="", notes="")
    eppstudent.save()

    sp = StudentPlacementsFactory(eppstudent=eppstudent, uin=person1,
                                  student_email="joejonas@xyz.com", university_supervisor_email="emily@xyz.com",
                                  university_supervisor="Emily Blake",
                                  cooperating_teacher_email="clark@xyz.com", cooperating_teacher="Clark Kent",
                                  principal="", site="", classroom_type="", semester="sprng",
                                  field_experience_program="", placement="",
                                  beginning_date_experience="2020-01-01", ending_date_experience="2021-01-01",
                                  instructor="")
    sp.save()

    tl = TimeLogsFactory(student_uin=person1, student_email="joejonas@xyz.com",
                         log_date="2022-04-07", notes="get test", hours_submitted=10, hours_approved=True,
                         approval_due_date="2022-04-13", semester="sprng", semester_year="2022",
                         start_time="2022-04-07T10:20:10.233-05:30", end_time="2022-04-07T20:20:10.233-05:30",
                         date_submitted="2022-04-06")
    tl.save()


@then("I click on the log in")
def step_impl(context):
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("joejonas@xyz.com")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("Password123*")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("student")
    context.browser.find_element_by_id("log-in-button").click()


@then("I am able to see my current timesheets submit page")
def step_impl(context):
    assert context.browser.current_url.endswith('/student/email/joejonas@xyz.com')


@then("I click on view previous timesheets")
def step_impl(context):
    time.sleep(1)
    context.browser.find_element_by_id("view_previous_timesheets").click()


@then("The previous timesheets are displayed")
def step_impl(context):
    assert context.browser.current_url.endswith('/prev/1')


@then("I click on View selected timesheets")
def step_impl(context):
    context.browser.find_element_by_id("view_selected_timesheets").click()


@then("I am able to view the selected timesheets")
def step_impl(context):
    current_week = get_current_week()
    current_week_monday = current_week["monday"]
    assert current_week_monday in context.browser.current_url


@then("I click on Submit Timesheets")
def step_impl(context):
    context.browser.find_element_by_id("submit_timesheets").click()


@then("I go to the submit timesheet webpage")
def step_impl(context):
    assert context.browser.current_url.endswith('/student/email/joejonas@xyz.com')


@then("I click on log out")
def step_impl(context):
    context.browser.find_element_by_id("logout-button").click()
    assert context.browser.current_url.endswith('/login/')
