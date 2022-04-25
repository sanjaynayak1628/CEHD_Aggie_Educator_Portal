# Created by sanjay at 23-04-2022
Feature: # Enter feature name here
  # As a co-op teacher
  # so that I can record the attendance of the students
  # I want to be able to view and approve timesheets submitted by my students

  Scenario: Cooperating teacher approve
    Given I am a registered cooperating teacher
    When I click the log in with cooperating teacher user type
    Then I am able to see the approve/reject timesheet
    Then I will click on the approve button
    Then The timesheets are approved and updated in the database
    Then I will click on the logout to logout

  Scenario: Cooperating teacher reject
    Given I am a registered cooperating teacher
    When I click the log in with cooperating teacher user type
    Then I am able to see the approve/reject timesheet
    Then I will click on the reject button
    Then The timesheets are rejected
    Then I will click on the logout to logout

  Scenario: Cooperating teacher view time sheet
    Given I am a registered cooperating teacher
    When I click the log in with cooperating teacher user type
    Then I am able to see the approve/reject timesheet
    Then I will click on the view time sheets button
    Then The previous timesheets webpage is displayed
    Then I will select a student
    Then I will be able to view the timesheets
    Then I will click on logout to logout
