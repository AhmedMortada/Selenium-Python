Feature: User Registration
    As a new user
    I want to register an account
    So that I can access the application

    Scenario: Successful user registration with valid data
        Given the user is on the registration page
        When the user enters a valid email address
        And the user enters a valid password
        And the user confirms the password
        And the user enters their full name
        And the user accepts the terms and conditions
        When the user clicks the register button
        Then the registration should be successful
        And the user should be redirected to the dashboard

    Scenario: Registration with invalid email format
        Given the user is on the registration page
        When the user enters an invalid email address
        And the user enters a valid password
        And the user confirms the password
        And the user enters their full name
        And the user accepts the terms and conditions
        When the user clicks the register button
        Then an error message about invalid email should be displayed

    Scenario: Registration with password mismatch
        Given the user is on the registration page
        When the user enters a valid email address
        And the user enters a valid password
        And the user enters a different password in confirm password
        And the user enters their full name
        And the user accepts the terms and conditions
        When the user clicks the register button
        Then an error message about password mismatch should be displayed

    Scenario: Registration without accepting terms
        Given the user is on the registration page
        When the user enters a valid email address
        And the user enters a valid password
        And the user confirms the password
        And the user enters their full name
        When the user clicks the register button
        Then an error message about accepting terms should be displayed 