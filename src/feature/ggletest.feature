
#Feature file of Automation Task to test Google Homepage

Feature: The Google logo image is present

  To check if Logo, Search fields and Search Button are present
  and to verify if search is performed with/without adding text is search field

Scenario: In order to verify if logo is present
    Given user navigates to homepage of Google "https://www.google.com"
    Then logo should be displayed
    And search text field should be displayed
    And Google search button should be present
    And Blank text should not preform
    And Check if text can be entered in search field
    Then Clicking on search button shows results



