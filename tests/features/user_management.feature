Feature: User Management Feature
    Background: Login To System
        Given User navigate to BASE_URL
        When User enter ADMIN_USER in username input
        And User enter ADMIN_PASSWORD in password input
        And User click login button

    Scenario Outline: Open Admin Page
        When User click on Admin menu
        When User hover on User Management submenu
        Then User should see Username input