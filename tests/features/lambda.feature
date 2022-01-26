Feature: lambda

    Background:
        Given I am logged in as testUser

    Scenario: Can run lambda
      When I run test_lambda lambda
      Then The lambda will pass