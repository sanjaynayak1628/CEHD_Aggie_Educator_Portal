# Created by sanjay at 23-04-2022
Feature: View Submitted Timesheets for Students
  # As a student,
  # so that I can check the approval status of the submitted timesheet
  # I want to be able to view timesheets

  Scenario: Student time log view
    Given I am a registered student to view
    Then I click on the log in
    Then I am able to see my current timesheets submit page
    Then I click on view previous timesheets
    Then The previous timesheets are displayed
    Then I click on View selected timesheets
    Then I am able to view the selected timesheets
    Then I click on Submit Timesheets
    Then I go to the submit timesheet webpage
    Then I click on log out
