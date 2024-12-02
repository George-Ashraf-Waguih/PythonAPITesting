
Feature: Github API Validation
  # Enter feature description here

  Scenario: session management check
    # Enter steps here
    Given I have github credentials
    When I hit getRepo API of github
    Then status code of response should be 200