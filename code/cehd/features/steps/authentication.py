from behave import *

use_step_matcher("re")


@given("we have a student")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have a student')


@when("a student successfully logins")
def step_impl(context):
    raise NotImplementedError(u'STEP: When a student logins')


@then("student timesheet should be opened")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then student timesheet should be opened')