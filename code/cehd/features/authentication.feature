# Created by sanjay at 20-03-2022
Feature: User Authentication
  # Enter feature description here

  Scenario: student authentication
    Given we have a student
    When a student logins with incorrect password
    Then error message should be displayed