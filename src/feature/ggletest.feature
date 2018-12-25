
#Feature file of Automation Task to test Google Homepage

Feature: Testing of Google Homepage

  To check if Logo, Search fields and Search Button are present
  and to verify if search is performed with/without adding text in search field

Scenario: In order to test Google Homepage
    Given user navigates to homepage of Google "https://www.google.com"
    Then logo should be displayed
    And search text field should be displayed
    And Google search button should be present
    And Blank text should not preform search
    And Check if text can be entered in search field
    Then Clicking on search button shows results



