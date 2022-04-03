# Created by Sanjay at 02-04-2022
Feature: Student Timesheet Submit View
  Scenario: Student time log save
    Given we have a student
    When a student save the timesheet
    Then the timesheet is saved in the database

  Scenario: Student time log update
    Given we have a student
    When a student updates the timesheet
    Then the timesheet is updated in the database

  Scenario: Student time log submit notification to cooperating teacher
    Given we have a student
    When a student submits the timesheet
    Then the cooperating teacher is notified via email
