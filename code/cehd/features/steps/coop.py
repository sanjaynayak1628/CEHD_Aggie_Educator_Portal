import time

from behave import *
from selenium.webdriver import Keys
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
        

@given("I am a registered cooperating teacher")
def step_impl(context):
    u = UserFactory(username='kent@xyz.com', email='kent@xyz.com')
    u.set_password('Password123*')
    u.save()

    person1 = PersonFactory(person_id=120, uin=120, netid="brucewayne", campus="CS", first_name="Bruce", middle_name="",
                            last_name="Wayne", use_middle_name=False, generation="", primary_email="brucewayne@xyz.com",
                            secondary_email="brucewaynesec@xyz.com", primary_ethnicity="X", latino=False,
                            country_of_origin="", sex="M", birth_date="1990-02-12", notes="",
                            last_updated_at="2022-04-03T10:20:10.233-05:30", last_updated_by=None, is_active=True,
                            is_admin=False, is_superuser=False, last_login_ip="10.0.0.21")
    person2 = PersonFactory(person_id=100, uin=100, netid="ryanreynolds", campus="CS", first_name="Ryan",
                            middle_name="", last_name="Reynolds", use_middle_name=False, generation="",
                            primary_email="ryanreynolds@xyz.com", secondary_email="ryan@xyz.com", primary_ethnicity="X",
                            latino=False, country_of_origin="", sex="M", birth_date="1985-02-12", notes="",
                            last_updated_at="2022-04-03T10:20:10.233-05:30",
                            last_updated_by=None, is_active=True, is_admin=False, is_superuser=False,
                            last_login_ip="10.0.0.21")
    person3 = PersonFactory(person_id=101, uin=101, netid="kent", campus="CS", first_name="Clark",
                            middle_name="", last_name="Kent", use_middle_name=False, generation="",
                            primary_email="kent@xyz.com", secondary_email="clark@xyz.com", primary_ethnicity="X",
                            latino=False, country_of_origin="", sex="M", birth_date="1985-02-12", notes="",
                            last_updated_at="2022-04-03T10:20:10.233-05:30",
                            last_updated_by=None, is_active=True, is_admin=False, is_superuser=False,
                            last_login_ip="10.0.0.21")
    person1.save()
    person2.save()
    person3.save()

    eppprogram = EPPProgramFactory(program_name="management course", program_abbreviation="mgmt",
                                   program_coordinator="",
                                   program_email="", initial=True, route="trad", has_teaching_fields=False,
                                   admission_notification_text="", auto_assigned_exams="", active=True)
    eppprogram.save()

    eppstudent = EPPStudentFactory(person=person1, program=eppprogram,
                                   first_name="Bruce", middle_name="", last_name="Wayne", cohort="", teaching_field="",
                                   teaid=1, admission_offer_date="2020-04-03", admission_acceptance_date="2020-04-13",
                                   admission_date="2020-05-03", admission_overall_gpa=4.0, admission_last60_gpa=4.0,
                                   subject_area_hours=20, subject_area_gpa=4.0, exit_status="", exit_semester="sprng",
                                   admission_reported_to_tea_date="2020-04-30", admission_offer_letter="",
                                   admission_acceptance_data="2020-04-13", previous_degree="B.S.",
                                   previous_degree_institution="Texas A&M University", previous_degree_date_month=5,
                                   previous_degree_date_year=2019, teaching_certificate_state="",
                                   teaching_certificate_expiration=1, classroom_experience=1.2,
                                   admission_offered_by=person3, additional_fields="", notes="")
    eppstudent.save()

    sp = StudentPlacementsFactory(eppstudent=eppstudent, uin=person1,
                                  student_email="brucewayne@xyz.com", university_supervisor_email="ryanreynolds@xyz.com",
                                  university_supervisor="Ryan Reynolds",
                                  cooperating_teacher_email="kent@xyz.com", cooperating_teacher="Clark Kent",
                                  principal="", site="", classroom_type="", semester="sprng",
                                  field_experience_program="", placement="",
                                  beginning_date_experience="2020-01-01", ending_date_experience="2021-01-01",
                                  instructor="")
    sp.save()

    tl = TimeLogsFactory(student_uin=person1, student_email="brucewayne@xyz.com",
                         log_date="2022-04-25", notes="test", hours_submitted=10, hours_approved=True,
                         approval_due_date="2022-05-03", semester="sprng", semester_year="2022",
                         start_time="2022-04-25T10:20:10.233-05:30", end_time="2022-04-25T20:20:10.233-05:30",
                         date_submitted="2022-04-26")
    tl.save()


@when("I click the log in with cooperating teacher user type")
def step_impl(context):
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("kent@xyz.com")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("Password123*")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("coop")
    context.browser.find_element_by_id("log-in-button").click()


@then("I am able to see the approve/reject timesheet")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com')


@then("I will click on the approve button")
def step_impl(context):
    # context.browser.find_element_by_id("approve-timesheet").send_keys(Keys.END)
    # time.sleep(0.5)
    submit = context.browser.find_element_by_id("approve-timesheet")
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com')


@then("The timesheets are approved and updated in the database")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com')


@then("I will click on the reject button")
def step_impl(context):
    # context.browser.find_element_by_id("reject-timesheet").send_keys(Keys.END)
    # time.sleep(0.5)
    submit = context.browser.find_element_by_id("reject-timesheet")
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com')


@then("The timesheets are rejected")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com')


@then("I will click on the view time sheets button")
def step_impl(context):
    context.browser.find_element_by_id("view_selected_timesheets").click()


@then("The previous timesheets webpage is displayed")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com/view')


@then("I will select a student")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com/view')


@then("I will be able to view the timesheets")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/kent@xyz.com/view')


@then("I will click on logout to logout")
def step_impl(context):
    time.sleep(1)
    context.browser.find_element_by_id("logout-button").click()
    assert context.browser.current_url.endswith('/login/')
