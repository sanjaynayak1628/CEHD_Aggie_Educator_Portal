import time
from behave import *
from test.factories.user import UserFactory
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

use_step_matcher("re")


@given("I am a registered supervisor")
def step_impl(context):
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='johnny@xyz.com', email='johnny@xyz.com')
    u.set_password('Password123*')
    # Don't omit to call save() to insert object in database
    u.save()


@then("I will click on log in button")
def step_impl(context):
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("johnny@xyz.com")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("Password123*")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("supervisor")
    context.browser.find_element_by_id("log-in-button").click()


@then("I will view the timesheets page for cooperating teachers under me")
def step_impl(context):
    assert context.browser.current_url.endswith('/supervisor/email/johnny@xyz.com')


@then("I will click on the logout button")
def step_impl(context):
    context.browser.find_element_by_id("logout-button").click()
    assert context.browser.current_url.endswith('/login/')
