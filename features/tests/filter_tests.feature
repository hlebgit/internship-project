# Created by hleb at 12/20/23
Feature: Filter by sale status Future Launch

  Scenario: User can filter by sale status Future Launch
    Given Open the main page
    When Log in to the page
    And Click on “off plan” at the left side menu
    And Verify the right page opens
    Then Filter by sale status of “Future Launch”
    And Verify each product contains the Future Launch tag