from behave import *

use_step_matcher("re")


@given("we have a student")
def step_impl(context):
    context.browser.get(context.base_url)
    username = context.browser.find_element_by_id("id_username")
    username.send_keys("sanjaynayak@tamu.edu")
    password = context.browser.find_element_by_id("id_password")
    password.send_keys("password")


@when("a student logins with incorrect password")
def step_impl(context):
    # find the button
    context.browser.find_element_by_xpath("//*[@id='signup-button']/button").click()


@then("error message should be displayed")
def step_impl(context):
    assert "Please enter a correct username and password. Note that both fields may be case-sensitive." == \
           context.browser.find_element_by_xpath("//ul[contains(@class, 'm-0')]//following::li[1]").get_attribute(
               'innerText')
