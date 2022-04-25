import time
from behave import *
from test.factories.user import UserFactory
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

use_step_matcher("re")


@given("I am a registered cooperating teacher")
def step_impl(context):
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='moore@xyz.com', email='moore@xyz.com')
    u.set_password('Password123*')
    # Don't omit to call save() to insert object in database
    u.save()


@when("I click the log in with cooperating teacher user type")
def step_impl(context):
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("moore@xyz.com")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("Password123*")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("coop")
    context.browser.find_element_by_id("log-in-button").click()


@then("I am able to see the approve/reject timesheet")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/moore@xyz.com/approve')


@then("I will click on the approve button")
def step_impl(context):
    context.browser.find_element_by_id("approve-timesheet").send_keys(Keys.END)
    time.sleep(0.5)
    submit = context.browser.find_element_by_id("approve-timesheet")


@then("The timesheets are approved and updated in the database")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/moore@xyz.com/approve')


@then("I will click on the logout to logout")
def step_impl(context):
    assert context.browser.current_url.endswith('/login/')


@then("I will click on the reject button")
def step_impl(context):
    context.browser.find_element_by_id("reject-timesheet").send_keys(Keys.END)
    time.sleep(0.5)
    submit = context.browser.find_element_by_id("reject-timesheet")


@then("The timesheets are rejected")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/moore@xyz.com/approve')


@then("I will click on the view time sheets button")
def step_impl(context):
    context.browser.find_element_by_id("view_selected_timesheets").send_keys(Keys.END)
    time.sleep(0.5)
    submit = context.browser.find_element_by_id("view_selected_timesheets")


@then("The previous timesheets webpage is displayed")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/moore@xyz.com/view')


@then("I will select a student")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/moore@xyz.com/view')


@then("I will be able to view the timesheets")
def step_impl(context):
    assert context.browser.current_url.endswith('/coop/email/moore@xyz.com/view')


@then("I will click on logout to logout")
def step_impl(context):
    context.browser.find_element_by_id("logout-button").click()
    assert context.browser.current_url.endswith('/login/')
