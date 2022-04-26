# Created by sanjay at 20-03-2022
Feature: User Authentication
  # As a student or cooperating teacher or supervisor
  # so that I can submit or view the timesheets
  # I want to be able to login into the application

  Scenario: student authentication fails
    Given we have a student
    When a student logins with incorrect password
    Then error message should be displayed for wrong password

  Scenario: student authentication fails
    Given we have a student
    When a student logins with incorrect username
    Then error message should be displayed for wrong username

  Scenario: student authentication passes
    Given we have a student
    When a student logins with correct username and password
    Then redirect to student profile submit timesheet
