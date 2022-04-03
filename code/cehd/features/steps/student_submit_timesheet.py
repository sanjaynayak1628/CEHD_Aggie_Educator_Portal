from behave import *

use_step_matcher("re")


@then("the timesheet is saved in the database")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the timesheet is saved in the database')


@when("a student save the timesheet")
def step_impl(context):
    raise NotImplementedError(u'STEP: When a student save the timesheet')


@when("a student updates the timesheet")
def step_impl(context):
    raise NotImplementedError(u'STEP: When a student updates the timesheet')


@then("the timesheet is updated in the database")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the timesheet is updated in the database')


@when("a student submits the timesheet")
def step_impl(context):
    raise NotImplementedError(u'STEP: When a student submits the timesheet')


@then("the cooperating teacher is notified via email")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cooperating teacher is notified via email')