from behave import *
from test.factories.user import UserFactory
from selenium.webdriver.support.ui import Select

use_step_matcher("re")


@given("we have a student")
def step_impl(context):
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('Password123*')
    # Don't omit to call save() to insert object in database
    u.save()


@when("a student logins with incorrect username")
def step_impl(context):
    # find the button
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("test@123.com")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("password")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("student")
    # context.browser.find_element_by_xpath("//*[@id='signup-button']/button").click()
    context.browser.find_element_by_id("log-in-button").click()


@then("error message should be displayed for wrong username")
def step_impl(context):
    assert "Please enter a correct username and password. Note that both fields may be case-sensitive." == \
           context.browser.find_element_by_xpath("//div[contains(@class, 'alert')]").get_attribute(
               'innerText')

@when("a student logins with incorrect password")
def step_impl(context):
    # find the button
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("foo")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("password")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("student")
    # context.browser.find_element_by_xpath("//*[@id='signup-button']/button").click()
    context.browser.find_element_by_id("log-in-button").click()


@then("error message should be displayed for wrong password")
def step_impl(context):
    assert "Please enter a correct username and password. Note that both fields may be case-sensitive." == \
           context.browser.find_element_by_xpath("//div[contains(@class, 'alert')]").get_attribute(
               'innerText')


@when("a student logins with correct username and password")
def step_impl(context):
    # find the button
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("foo")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("Password123*")
    usertype = Select(context.browser.find_element_by_id("usertype"))
    usertype.select_by_value("student")
    # context.browser.find_element_by_xpath("//*[@id='signup-button']/button").click()
    context.browser.find_element_by_id("log-in-button").click()


@then("redirect to student profile submit timesheet")
def step_impl(context):
    cb = context.browser
    # print(cb.current_url, '-----------------------')
    assert cb.current_url.endswith('/timelogs/student/email/foo')
