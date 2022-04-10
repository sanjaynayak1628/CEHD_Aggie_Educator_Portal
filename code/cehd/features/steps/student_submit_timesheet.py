import time
from behave import *
from test.factories.user import UserFactory
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")


@given("I am a registered student")
def step_impl(context):
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='abc@xyz.com', email='abc@xyz.com')
    u.set_password('Password123*')
    # Don't omit to call save() to insert object in database
    u.save()


@when("I click on the log in")
def step_impl(context):
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("abc@xyz.com")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("Password123*")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("student")
    context.browser.find_element_by_id("log-in-button").click()


@then("I am able to see my time sheet page")
def step_impl(context):
    assert context.browser.current_url.endswith('/timelogs/student/email/abc@xyz.com')


@then("I will add the time for the days")
def step_impl(context):
    tr = ["_notes", "_stime", "_etime", "_hours"]
    td = {
        "1": ["monday timesheet", "09:00AM", "10:00AM", "1"],
        "2": ["tuesday timesheet", "09:00AM", "10:00AM", "1"],
        "3": ["wednesday timesheet", "09:00AM", "10:00AM", "1"],
        "4": ["thursday timesheet", "09:00AM", "10:00AM", "1"],
        "5": ["friday timesheet", "09:00AM", "10:00AM", "1"],
        "6": ["saturday timesheet", "09:00AM", "10:00AM", "1"],
        "7": ["sunday timesheet", "09:00AM", "10:00AM", "1"]
    }
    for k, v in td.items():
        for i in range(len(tr)):
            context.browser.find_element_by_id(k + tr[i]).send_keys(v[i])


@then("I will click on the save")
def step_impl(context):
    # scroll to end and click on Save button
    context.browser.find_element_by_id("save-timesheet").send_keys(Keys.END)
    time.sleep(0.5)
    save = context.browser.find_element_by_id("save-timesheet")
    # webdriver.ActionChains(context.browser).move_to_element(save).click().perform()


@then("the timesheet is saved in the database")
def step_impl(context):
    assert context.browser.current_url.endswith('/timelogs/student/email/abc@xyz.com')


@then("I click on the log out button")
def step_impl(context):
    context.browser.find_element_by_id("logout-button").click()
    assert context.browser.current_url.endswith('/logout/')


@then("I will update the time for the days")
def step_impl(context):
    tr = ["_notes", "_stime", "_etime", "_hours"]
    td = {
        "1": ["monday timesheet", "09:00AM", "10:00AM", "1"],
        "2": ["tuesday timesheet", "09:00AM", "10:00AM", "1"],
        "3": ["wednesday timesheet", "09:00AM", "12:00PM", "3"],
        "4": ["thursday timesheet", "09:00AM", "10:00AM", "1"],
        "5": ["friday timesheet", "09:00AM", "10:00AM", "1"],
        "6": ["saturday timesheet", "09:00AM", "10:00AM", "1"],
        "7": ["sunday timesheet", "09:00AM", "10:00AM", "1"]
    }
    for k, v in td.items():
        for i in range(len(tr)):
            context.browser.find_element_by_id(k + tr[i]).send_keys(v[i])


@then("I will click on the submit")
def step_impl(context):
    # scroll to end and click on Save button
    context.browser.find_element_by_id("submit-timesheet").send_keys(Keys.END)
    time.sleep(0.5)
    submit = context.browser.find_element_by_id("submit-timesheet")


@then("the timesheet is submitted in the database")
def step_impl(context):
    assert context.browser.current_url.endswith('/timelogs/student/email/abc@xyz.com')
