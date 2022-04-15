# Created by Sanjay at 02-04-2022
Feature: Student Timesheet Submit View
  Scenario: Student time log save
    Given I am a registered student
    When I click on the log in
    Then I am able to see my time sheet page
    Then I will add the time for the days
    Then I will click on the save
    Then the timesheet is saved in the database
    Then I click on the log out button

  Scenario: Student time log update
    Given I am a registered student
    When I click on the log in
    Then I am able to see my time sheet page
    Then I will update the time for the days
    Then I will click on the save
    Then the timesheet is saved in the database
    Then I click on the log out button

  Scenario: Student time log submit
    Given I am a registered student
    When I click on the log in
    Then I am able to see my time sheet page
    Then I will add the time for the days
    Then I will click on the submit
    Then the timesheet is submitted in the database
    Then I click on the log out button
