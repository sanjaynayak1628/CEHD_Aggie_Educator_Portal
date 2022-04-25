import time
from behave import *
from test.factories.user import UserFactory
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

use_step_matcher("re")


@given("I am a registered student to view")
def step_impl(context):
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='abc@xyz.com', email='abc@xyz.com')
    u.set_password('Password123*')
    # Don't omit to call save() to insert object in database
    u.save()


@then("I click on the log in")
def step_impl(context):
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("abc@xyz.com")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("Password123*")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("student")
    context.browser.find_element_by_id("log-in-button").click()


@then("I am able to see my current timesheets submit page")
def step_impl(context):
    assert context.browser.current_url.endswith('/student/email/abc@xyz.com')


@then("I click on view previous timesheets")
def step_impl(context):
    context.browser.find_element_by_id("view_previous_timesheets").click()


@then("The previous timesheets are displayed")
def step_impl(context):
    assert context.browser.current_url.endswith('/prev/1')


@then("I click on View selected timesheets")
def step_impl(context):
    context.browser.find_element_by_id("view_selected_timesheets").click()


@then("I am able to view the selected timesheets")
def step_impl(context):
    assert context.browser.current_url.endswith('/prev/1')


@then("I click on Submit Timesheets")
def step_impl(context):
    context.browser.find_element_by_id("submit_timesheets").click()


@then("I go to the submit timesheet webpage")
def step_impl(context):
    assert context.browser.current_url.endswith('/student/email/abc@xyz.com')


@then("I click on log out")
def step_impl(context):
    context.browser.find_element_by_id("logout-button").click()
    assert context.browser.current_url.endswith('/login/')
