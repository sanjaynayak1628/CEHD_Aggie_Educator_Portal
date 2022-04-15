# import time
# from behave import *
# from selenium.webdriver import Keys
# from test.factories.user import UserFactory
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# use_step_matcher("re")
#
#
# @given("we have a registered student in the student timesheet submit page")
# def step_impl(context):
#     # Creates a dummy user for our tests (user is not authenticated at this point)
#     u = UserFactory(username='abc@xyz.com', email='abc@xyz.com')
#     u.set_password('Password123*')
#     # Don't omit to call save() to insert object in database
#     u.save()
#     context.browser.get(context.base_url)
#     username = context.browser.find_element_by_id("id_username")
#     username.send_keys("abc@xyz.com")
#     password = context.browser.find_element_by_id("id_password")
#     password.send_keys("Password123*")
#     usertype = Select(context.browser.find_element_by_id("usertype"))
#     usertype.select_by_value("student")
#     # context.browser.find_element_by_xpath("//*[@id='signup-button']/button").click()
#     context.browser.find_element_by_id("log-in-button").click()
#
#
# # @then("the timesheet is saved in the database")
# # def step_impl(context):
# #     wait = WebDriverWait(context.browser, 5)
# #     wait.until(EC.alert_is_present())
# #     alert = context.browser.switch_to.alert
# #     assert "Entered time entries saved successfully" in alert.text
# #     alert.accept()
# #     context.browser.find_element_by_id("logout-button").click()
#
#
# @when("a student save the timesheet")
# def step_impl(context):
#     tr = ["_notes", "_stime", "_etime", "_hours"]
#     td = {
#         "1": ["monday timesheet", "09:00AM", "10:00AM", "1"],
#         "2": ["tuesday timesheet", "09:00AM", "10:00AM", "1"],
#         "3": ["wednesday timesheet", "09:00AM", "10:00AM", "1"],
#         "4": ["thursday timesheet", "09:00AM", "10:00AM", "1"],
#         "5": ["friday timesheet", "09:00AM", "10:00AM", "1"],
#         "6": ["saturday timesheet", "09:00AM", "10:00AM", "1"],
#         "7": ["sunday timesheet", "09:00AM", "10:00AM", "1"]
#     }
#     for k, v in td.items():
#         for i in range(len(tr)):
#             context.browser.find_element_by_id(k+tr[i]).send_keys(v[i])
#     # scroll to end and click on Save button
#     context.browser.find_element_by_id("save-timesheet").send_keys(Keys.END)
#     time.sleep(0.5)
#     save = context.browser.find_element_by_id("save-timesheet")
#     webdriver.ActionChains(context.browser).move_to_element(save).click().perform()
#
#
# @when("a student updates the timesheet")
# def step_impl(context):
#     tr = ["_notes", "_stime", "_etime", "_hours"]
#     td = {
#         "1": ["monday timesheet", "09:00AM", "12:00PM", "3"],
#         "2": ["tuesday timesheet", "09:00AM", "10:00AM", "1"],
#         "3": ["wednesday timesheet", "09:00AM", "11:00AM", "2"],
#         "4": ["thursday timesheet", "09:00AM", "10:00AM", "1"],
#         "5": ["friday timesheet", "09:00AM", "10:00AM", "1"]
#     }
#     for k, v in td.items():
#         for i in range(len(tr)):
#             context.browser.find_element_by_id(k + tr[i]).send_keys(v[i])
#     context.browser.find_element_by_id("save_timesheet").click()
#
#
# @then("the timesheet is updated in the database")
# def step_impl(context):
#     wait = WebDriverWait(context.browser, 5)
#     wait.until(EC.alert_is_present())
#     alert = context.browser.switch_to.alert
#     assert "Entered time entries saved successfully" in alert.text
#     alert.accept()
#     context.browser.find_element_by_id("logout-button").click()
#
#
# @when("a student submits the timesheet")
# def step_impl(context):
#     tr = ["_notes", "_stime", "_etime", "_hours"]
#     td = {
#         "1": ["monday timesheet", "09:00AM", "11:00AM", "2"],
#         "2": ["tuesday timesheet", "09:00AM", "10:00AM", "1"],
#         "3": ["wednesday timesheet", "09:00AM", "11:00AM", "2"],
#         "4": ["thursday timesheet", "09:00AM", "11:00AM", "2"],
#         "5": ["friday timesheet", "09:00AM", "11:00AM", "2"]
#     }
#     for k, v in td.items():
#         for i in range(len(tr)):
#             context.browser.find_element_by_id(k + tr[i]).send_keys(v[i])
#     context.browser.find_element_by_id("submit_timesheet").click()
#
#
# @then("the timesheet is submitted in the database")
# def step_impl(context):
#     wait = WebDriverWait(context.browser, 5)
#     wait.until(EC.alert_is_present())
#     alert = context.browser.switch_to.alert
#     assert "Entered time entries submitted successfully" in alert.text
#     alert.accept()
#     context.browser.find_element_by_id("logout-button").click()
#
#
# # @then("the cooperating teacher is notified via email")
# # def step_impl(context):
# #     raise NotImplementedError(u'STEP: Then the cooperating teacher is notified via email')
