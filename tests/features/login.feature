Feature: Login

    Demonstrate login
    Scenario Outline: Login With Valid Credentials
        Given User navigate to <homepage>
        When User enter <username> in username input
        And User enter <password> in password input
        And User click login button
        Then User should be navigate to Dashboard page

        Examples:
            | homepage | username   | password       |
            | BASE_URL | ADMIN_USER | ADMIN_PASSWORD |

    Scenario Outline: Login With Invalid Credentials
        Given User navigate to <homepage>
        When User enter <username> in username input
        And User enter <password> in password input
        And User click login button
        Then User should see an error message
        And Error message should be <error_message>

        Examples:
            | homepage | username     | password         | error_message       |
            | BASE_URL | INVALID_USER | INVALID_PASSWORD | Invalid credentials |
